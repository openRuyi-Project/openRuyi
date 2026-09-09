# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nats-streaming-server
%define go_import_path  github.com/nats-io/nats-streaming-server
%define commit_id       d51efd0496575cf0d7325c7f147932007598f243

Name:           go-github-nats-io-nats-streaming-server
Version:        0+git20261127.d51efd0
Release:        %autorelease
Summary:        Reusable Go source for NATS Streaming
License:        Apache-2.0
URL:            https://github.com/nats-io/nats-streaming-server
#!RemoteAsset:  sha256:13d056d465e2a71de64bd19bf8a60ccaf8c8dbdf5490656866675404ab1520cc
Source0:        https://github.com/nats-io/nats-streaming-server/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix historical test format strings rejected by current Go vet.
Patch2000:      2000-fix-test-format-strings.patch
# Wait for NATS route propagation before the duplicate-ID test assertion.
Patch2001:      2001-wait-for-route-before-duplicate-check.patch
# Report standalone readiness only after graceful signal handling is installed.
Patch2002:      2002-report-ready-after-installing-signal-handlers.patch
# Wait for asynchronous cleanup without weakening the connection leak limit.
Patch2003:      2003-wait-for-raft-connection-cleanup.patch
# Current nats-server ResponseHandler ignores JSONP callbacks and returns JSON.
Patch2004:      2004-expect-json-for-removed-nats-jsonp.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-sql-driver/mysql)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-msgpack)
BuildRequires:  go(github.com/hashicorp/raft)
BuildRequires:  go(github.com/lib/pq)
BuildRequires:  go(github.com/nats-io/nats-server/v2)
BuildRequires:  go(github.com/nats-io/nats.go)
BuildRequires:  go(github.com/nats-io/nuid)
BuildRequires:  go(github.com/nats-io/stan.go)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(go.etcd.io/bbolt)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/nats-io/nats-streaming-server) = %{version}

Requires:       go(github.com/go-sql-driver/mysql)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/hashicorp/go-hclog)
Requires:       go(github.com/hashicorp/go-msgpack)
Requires:       go(github.com/hashicorp/raft)
Requires:       go(github.com/lib/pq)
Requires:       go(github.com/nats-io/nats-server/v2)
Requires:       go(github.com/nats-io/nats.go)
Requires:       go(github.com/nats-io/nuid)
Requires:       go(github.com/nats-io/stan.go)
Requires:       go(github.com/prometheus/procfs)
Requires:       go(go.etcd.io/bbolt)
Requires:       go(golang.org/x/crypto)

%description
Reusable server, protocol and storage Go packages for NATS Streaming,
matching the snapshot pinned by stan.go 0.10.4 integration tests.

%check
%{go_common}
mkdir -p %{_builddir}/go/src/%{go_import_path}
cp -a . %{_builddir}/go/src/%{go_import_path}
cd %{_builddir}/go/src/%{go_import_path}
# Signal tests invoke a temporary helper executable from PATH; do not ship it.
%__go build -o %{_builddir}/test-bin/%{_name} .
export PATH="%{_builddir}/test-bin:$PATH"
nats_skip_args=()
if [ "$(%__go env GOARCH)" = riscv64 ]; then
    # The fixture's 250 ms channel expiry races snapshot I/O on OBS workers.
    nats_skip_args=(-skip '^TestClusteringFollowerDeleteOldChannelPriorToSnapshotRestore$')
fi
# Default golangmodules check cannot place -sql=false after package paths.
for test_package in $(%__go list ./...); do
    %__go test %{shrink:%{go_test_flags_default}} -timeout 20m         "${nats_skip_args[@]}" "$test_package" -sql=false
done

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
