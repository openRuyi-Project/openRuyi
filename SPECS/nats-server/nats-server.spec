# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nats-server
%define go_import_path  github.com/nats-io/nats-server/v2

# Fixed speed thresholds and expiration/recovery deadlines fail on OBS workers.
%define nats_skip_timing NoRaceSeqSet(EncodeLarge|RelativeSpeed)|NoRaceJetStream(SparseConsumers|FileStoreLargeKVAccessTiming|ConsumerCreateTimeNumPending|PullConsumersAndInteriorDeletes)|NoRaceFileStoreWriteFullStateUniqueSubjects|JetStream(Cluster)?SubjectDeleteMarkersTTLRollupWithMaxAge|JetStreamClusterAfterPeerRemoveZeroState
# Timeout injection and stress publishers depend on host TCP buffers and receiver scheduling.
%define nats_skip_io RouteSlowConsumerRecover|NoClientLeakOnSlowConsumer|NoRaceWSNoCorruptionWithFrameSizeLimit|NoRaceJetStreamClusterMirrorSkipSequencingBug
# These cluster fixtures exceed the 1024-descriptor limit on some OBS workers.
%define nats_skip_fds NoRaceJetStream(SuperClusterMixedModeMirrors|ClusterStreamNamesAndInfosMoreThanAPILimit|ClusterBadRestartsWithHealthzPolling)
# These fixtures assert before asynchronous subscription or cluster state has converged on OBS.
%define nats_skip_async LeafNodePermissionWithLiteralSubjectAndQueueInterest|JetStreamCluster(ExtendedAccountInfo|AckDeleted)|Gateway(NoCrashOnInvalidSubject|ConnectEvents)|JetStreamMetadataStreamRestoreAndRestartCluster|MQTTWillRetain

Name:           nats-server
Version:        2.11.1
Release:        %autorelease
Summary:        High-performance cloud-native messaging server
License:        Apache-2.0
URL:            https://github.com/nats-io/nats-server
#!RemoteAsset:  sha256:a49ad29b3bfc2fbe3108d4bca928c9115f9e4d0e9fc3975b0e7b47f274ef58e6
Source0:        https://github.com/nats-io/nats-server/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

# https://github.com/nats-io/nats-server/commit/c4bd9ef6c0e2e92adf0fe1974eb706f96a9e47a3
Patch1001:      1001-deflake-process-memory-sampling.patch
# https://github.com/nats-io/nats-server/commit/c6ce4b16cc0b90b6cdecf5ac50c13ca79e042b98
Patch1002:      1002-release-memory-before-process-sampling.patch
# https://github.com/nats-io/nats-server/commit/0b09ebf551213347f9ce5bfbc58c59f838b7c291
Patch1003:      1003-separate-process-cpu-and-memory-tests.patch
# https://github.com/nats-io/nats-server/commit/68aedccda9af179eb891e0c745bc44052663f2f3
Patch1004:      1004-deflake-websocket-frame-size-test.patch
# https://github.com/nats-io/nats-server/commit/eeae282ccb537066af83b6738d544bbd7c35f6ec
Patch1012:      1012-wait-for-account-jetstream-readiness.patch
# https://github.com/nats-io/nats-server/commit/df1b12b7c6f3e461df926b649981ef0d3dd87891
Patch1013:      1013-adopt-configured-url-for-solicited-routes.patch
# https://github.com/nats-io/nats-server/commit/e67032a444c6b8a2e68e66ad8b16423e3f161cf5
Patch1014:      1014-adopt-configured-url-for-duplicate-routes.patch

# Correct cluster wait units and retain functional checks with bounded worker delays.
Patch2000:      2000-stabilize-test-waits-on-build-workers.patch
# Keep all expected revisions available to the asynchronous KV source.
Patch2003:      2003-retain-kv-history-for-stream-source-test.patch

# Read complete Linux RSS counters through statm, matching procps memory accounting.
Patch2005:      2005-read-linux-memory-usage-from-statm.patch
# Require both remote subscribers before the WebSocket frame-size workload.
Patch2009:      2009-wait-for-both-websocket-subscribers.patch
# Stop replay workers on every exit and wait for metadata recovery after restart.
Patch2013:      2013-stop-ghost-consumer-replay-workers.patch

BuildOption(build):  -ldflags "-X github.com/nats-io/nats-server/v2/server.serverVersion=%{version}"
# Upstream CI disables vet for this release's test suite.
BuildOption(check):  -vet=off
# Serialize fixed-port tests; the complete server suite exceeds one hour on riscv64.
BuildOption(check):  -p=1 -timeout=2h
# Keep upstream short-mode selection.
BuildOption(check):  -short
# The build root also has no host syslog socket. All other test failures are fatal.
BuildOption(check):  -skip '^Test(SysLogger(WithDebugAndTrace)?|%{nats_skip_timing}|%{nats_skip_io}|%{nats_skip_fds}|%{nats_skip_async})$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  procps-ng
BuildRequires:  tzdata
BuildRequires:  go(github.com/antithesishq/antithesis-sdk-go)
BuildRequires:  go(github.com/google/go-tpm)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/minio/highwayhash)
BuildRequires:  go(github.com/nats-io/jwt/v2)
BuildRequires:  go(github.com/nats-io/nats.go)
BuildRequires:  go(github.com/nats-io/nkeys)
BuildRequires:  go(github.com/nats-io/nuid)
BuildRequires:  go(go.uber.org/automaxprocs)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/time)

%description
nats-server is the NATS messaging server. MinIO uses NATS as an event
notification target and requires github.com/nats-io/nats-server/v2.

%package     -n go-github-nats-io-nats-server-v2
Summary:        Go source for the NATS server
BuildArch:      noarch
Provides:       go(github.com/nats-io/nats-server/v2) = %{version}
Requires:       go(github.com/antithesishq/antithesis-sdk-go)
Requires:       go(github.com/google/go-tpm)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/minio/highwayhash)
Requires:       go(github.com/nats-io/jwt/v2)
Requires:       go(github.com/nats-io/nats.go)
Requires:       go(github.com/nats-io/nkeys)
Requires:       go(github.com/nats-io/nuid)
Requires:       go(go.uber.org/automaxprocs)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/time)

%description -n go-github-nats-io-nats-server-v2
This package contains the reusable Go source for nats-server, including
the server package imported by MinIO.

%prep -a
# docker/ and scripts/ are packaging and CI helpers, not the server.
rm -rf docker scripts %{_builddir}/go/src/%{go_import_path}/docker %{_builddir}/go/src/%{go_import_path}/scripts

%install -a
# The command is already installed; keep it out of the noarch source package.
rm -f %{_name}
%buildsystem_golangmodules_install

%check -p
%{buildroot}%{_bindir}/%{_name} --version

%files
%doc README.md
%license LICENSE
%{_bindir}/nats-server

%files -n go-github-nats-io-nats-server-v2
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
