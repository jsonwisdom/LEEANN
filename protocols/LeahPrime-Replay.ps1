# LeahPrime Protocol One — Machine-Speed Historical Replay
# Authority_Created: false
# Mode: REPLAY only (no silent promotion)
# Instance: Mildenhall / UK Edition
# Codename surface: GrayBaby · CrissCross · AppleSauce
#
# Doctrine:
# - An ExpectedHead argument is not proof of a head match.
# - The historical target is replayed in a detached temporary worktree.
# - Exact source bytes are SHA-256 checked before PASS can be emitted.
# - -Promote is intentionally blocked while schema/timestamp holds remain.

param(
    [switch]$Promote,
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[0-9a-fA-F]{40}$')]
    [string]$ExpectedHead,
    [string]$ReceiptPath = ".\LeahPrimeProtocolOne.receipt.json"
)

$ErrorActionPreference = "Stop"
if (Get-Variable PSNativeCommandUseErrorActionPreference -ErrorAction SilentlyContinue) {
    $PSNativeCommandUseErrorActionPreference = $false
}

$timestamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
$ExpectedHead = $ExpectedHead.ToLowerInvariant()

# Canonical source-byte digests previously reproduced by the exact-head replay.
# These identify file bytes at the historical target; they are not Git blob IDs.
$ExpectedGenesisSha256 = "1f6d812fc30582c482d0ce8233347dd8878901ebda2c90fa6e2545918036830c"
$ExpectedDannellySha256 = "5ac3260b6b90c0f221e9fc4302a85f163dd088b9f27f5911daa384c22c85ea99"
$DigestEvidence = "GitHub Actions run 31840989464 / canonical-head replay"

$RepoRoot = (& git rev-parse --show-toplevel).Trim()
if ($LASTEXITCODE -ne 0 -or -not $RepoRoot) {
    throw "Protocol One must run inside a Git repository."
}

$HarnessHead = (& git rev-parse HEAD).Trim().ToLowerInvariant()
$ReceiptFullPath = if ([System.IO.Path]::IsPathRooted($ReceiptPath)) {
    [System.IO.Path]::GetFullPath($ReceiptPath)
} else {
    [System.IO.Path]::GetFullPath((Join-Path (Get-Location).Path $ReceiptPath))
}
$ReceiptDir = Split-Path -Parent $ReceiptFullPath
New-Item -ItemType Directory -Force -Path $ReceiptDir | Out-Null

$WorktreePath = Join-Path ([System.IO.Path]::GetTempPath()) ("leahprime-protocol-one-" + [guid]::NewGuid().ToString("N"))
$ReplayTempDir = Join-Path ([System.IO.Path]::GetTempPath()) ("leahprime-replay-receipt-" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Force -Path $ReplayTempDir | Out-Null
$StructuralReceiptPath = Join-Path $ReplayTempDir "GENESIS_EXECUTABLE_REPLAY_RECEIPT_V0_1.json"

$holds = [System.Collections.Generic.List[string]]::new()
$holds.Add("SCHEMA_COMPLIANCE")
$holds.Add("TIMESTAMP_RELATION")
$errors = [System.Collections.Generic.List[string]]::new()

$result = [ordered]@{
    protocol             = "LeahPrime_Protocol_One"
    version              = "1.0"
    instance             = "Mildenhall_UK"
    codenames            = @("GrayBaby", "CrissCross", "AppleSauce")
    timestamp_utc        = $timestamp
    mode                 = "REPLAY"
    status               = "NOT_RUN"
    authority_created    = $false
    facts_promoted       = 0
    promotion_gate       = "CLOSED"
    bitbot_validator     = "CLOSED"
    holds                = @()
    errors               = @()
    harness              = [ordered]@{
        repository_head = $HarnessHead
        script_path     = "protocols/LeahPrime-Replay.ps1"
    }
    historical_target   = [ordered]@{
        expected_head = $ExpectedHead
        actual_head   = $null
        head_match    = $false
    }
    source_bytes        = [ordered]@{
        evidence = $DigestEvidence
        genesis = [ordered]@{
            path            = "timegraph/TIMEGRAPH_GENESIS_BLOCK_V0_1.json"
            expected_sha256 = $ExpectedGenesisSha256
            computed_sha256 = $null
            match           = $false
        }
        dannelly_fixture = [ordered]@{
            path            = "fixtures/timegraph/DANNELLY_MIXED_PACKET_GENESIS_FIXTURE_V0_1.json"
            expected_sha256 = $ExpectedDannellySha256
            computed_sha256 = $null
            match           = $false
        }
    }
    structural_replay    = [ordered]@{
        harness_path = "tools/replay_timegraph_genesis_v0_1.py"
        exit_code    = $null
        overall      = $null
        sequence     = $null
        classification = $null
        rail_collapse = $null
        facts_promoted = $null
    }
    source_replay        = "NOT_RUN"
}

Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host " LeahPrime Protocol One — Historical Machine Replay" -ForegroundColor Cyan
Write-Host " Instance : Mildenhall / UK Edition" -ForegroundColor DarkCyan
Write-Host " Surface  : GrayBaby · CrissCross · AppleSauce" -ForegroundColor DarkCyan
Write-Host " Target   : $ExpectedHead" -ForegroundColor Yellow
Write-Host " Mode     : REPLAY (promotion closed)" -ForegroundColor Yellow
Write-Host "═══════════════════════════════════════════════════"

try {
    # Prove the requested historical commit exists before creating the worktree.
    & git cat-file -e "$ExpectedHead`^{commit}" 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "Expected historical commit does not exist in this repository: $ExpectedHead"
    }

    Write-Host "`n[HEAD] Creating detached worktree for exact historical target..." -ForegroundColor Green
    & git worktree add --detach $WorktreePath $ExpectedHead | Out-Host
    if ($LASTEXITCODE -ne 0) {
        throw "git worktree add failed."
    }

    $ActualHead = (& git -C $WorktreePath rev-parse HEAD).Trim().ToLowerInvariant()
    $result.historical_target.actual_head = $ActualHead
    $result.historical_target.head_match = ($ActualHead -eq $ExpectedHead)
    if (-not $result.historical_target.head_match) {
        throw "Historical target mismatch: expected=$ExpectedHead actual=$ActualHead"
    }

    Write-Host "[HEAD] exact historical HEAD verified: $ActualHead" -ForegroundColor Green

    $GenesisPath = Join-Path $WorktreePath "timegraph/TIMEGRAPH_GENESIS_BLOCK_V0_1.json"
    $DannellyPath = Join-Path $WorktreePath "fixtures/timegraph/DANNELLY_MIXED_PACKET_GENESIS_FIXTURE_V0_1.json"

    if (-not (Test-Path -LiteralPath $GenesisPath)) { throw "Genesis artifact missing at historical target." }
    if (-not (Test-Path -LiteralPath $DannellyPath)) { throw "Dannelly fixture missing at historical target." }

    $GenesisHash = (Get-FileHash -LiteralPath $GenesisPath -Algorithm SHA256).Hash.ToLowerInvariant()
    $DannellyHash = (Get-FileHash -LiteralPath $DannellyPath -Algorithm SHA256).Hash.ToLowerInvariant()

    $result.source_bytes.genesis.computed_sha256 = $GenesisHash
    $result.source_bytes.genesis.match = ($GenesisHash -eq $ExpectedGenesisSha256)
    $result.source_bytes.dannelly_fixture.computed_sha256 = $DannellyHash
    $result.source_bytes.dannelly_fixture.match = ($DannellyHash -eq $ExpectedDannellySha256)

    if (-not $result.source_bytes.genesis.match) {
        $errors.Add("GENESIS_SHA256_MISMATCH")
    }
    if (-not $result.source_bytes.dannelly_fixture.match) {
        $errors.Add("DANNELLY_SHA256_MISMATCH")
    }

    Write-Host "[SHA256] Genesis : $GenesisHash" -ForegroundColor Cyan
    Write-Host "[SHA256] Dannelly: $DannellyHash" -ForegroundColor Cyan

    Write-Host "`n[REPLAY] Executing committed structural harness inside historical worktree..." -ForegroundColor Green
    Push-Location $WorktreePath
    try {
        $PythonLines = & python "tools/replay_timegraph_genesis_v0_1.py" --out $StructuralReceiptPath 2>&1
        $PythonExit = $LASTEXITCODE
    } finally {
        Pop-Location
    }

    $result.structural_replay.exit_code = $PythonExit
    if ($PythonLines) { $PythonLines | ForEach-Object { Write-Host $_ } }

    if ($PythonExit -ne 0) {
        $errors.Add("STRUCTURAL_REPLAY_EXIT_$PythonExit")
    } elseif (-not (Test-Path -LiteralPath $StructuralReceiptPath)) {
        $errors.Add("STRUCTURAL_RECEIPT_MISSING")
    } else {
        $Structural = Get-Content -LiteralPath $StructuralReceiptPath -Raw | ConvertFrom-Json
        $result.structural_replay.overall = $Structural.overall
        $result.structural_replay.sequence = $Structural.replay.sequence_status
        $result.structural_replay.classification = $Structural.replay.classification_status
        $result.structural_replay.rail_collapse = $Structural.replay.fixture_observed.rail_collapse
        $result.structural_replay.facts_promoted = $Structural.replay.facts_promoted

        if ($Structural.overall -ne "STRUCTURAL_PASS_WITH_HOLDS") { $errors.Add("STRUCTURAL_OVERALL_NOT_PASS_WITH_HOLDS") }
        if ($Structural.replay.sequence_status -ne "PASS") { $errors.Add("SEQUENCE_NOT_PASS") }
        if ($Structural.replay.classification_status -ne "PASS") { $errors.Add("CLASSIFICATION_NOT_PASS") }
        if ($Structural.replay.fixture_observed.rail_collapse -ne $false) { $errors.Add("RAIL_COLLAPSE_TRUE") }
        if ([int]$Structural.replay.facts_promoted -ne 0) { $errors.Add("FACT_PROMOTION_NONZERO") }
    }

    if ($result.historical_target.head_match -and
        $result.source_bytes.genesis.match -and
        $result.source_bytes.dannelly_fixture.match -and
        $PythonExit -eq 0 -and
        $errors.Count -eq 0) {
        $result.source_replay = "PASS"
        $result.status = "PASS_WITH_HOLDS"
    } else {
        $result.source_replay = "FAIL"
        $result.status = "FAIL"
    }

    # Promotion remains intentionally impossible in Protocol One v1.0.
    if ($Promote) {
        Write-Host "`n[GATE] -Promote detected; promotion remains LOCKED by doctrine." -ForegroundColor Red
        $result.mode = "REPLAY_PROMOTE_ATTEMPTED_BUT_BLOCKED"
        $holds.Add("PROMOTION_BLOCKED_BY_DOCTRINE")
    } else {
        Write-Host "`n[GATE] No -Promote switch. Remaining in REPLAY mode." -ForegroundColor Yellow
    }

    $result.facts_promoted = 0
    $result.authority_created = $false
    $result.promotion_gate = "CLOSED"
    $result.bitbot_validator = "CLOSED"
}
catch {
    $errors.Add($_.Exception.Message)
    $result.status = "FAIL"
    $result.source_replay = "FAIL"
    Write-Host "`n[FAIL] $($_.Exception.Message)" -ForegroundColor Red
}
finally {
    if (Test-Path -LiteralPath $WorktreePath) {
        & git worktree remove --force $WorktreePath 2>$null | Out-Null
    }
    if (Test-Path -LiteralPath $ReplayTempDir) {
        Remove-Item -LiteralPath $ReplayTempDir -Recurse -Force -ErrorAction SilentlyContinue
    }
}

$result.holds = @($holds)
$result.errors = @($errors)

$result | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $ReceiptFullPath -Encoding UTF8
$ReceiptHash = (Get-FileHash -LiteralPath $ReceiptFullPath -Algorithm SHA256).Hash.ToLowerInvariant()

Write-Host "`n[RECEIPT] Written -> $ReceiptFullPath" -ForegroundColor Cyan
Write-Host "          receipt_sha256   : $ReceiptHash" -ForegroundColor Cyan
Write-Host "          authority_created: $($result.authority_created)" -ForegroundColor Cyan
Write-Host "          facts_promoted   : $($result.facts_promoted)" -ForegroundColor Cyan
Write-Host "          status           : $($result.status)" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════`n"

if ($result.status -eq "FAIL") {
    exit 1
}
