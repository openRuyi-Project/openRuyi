# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nats-server
%define go_import_path  github.com/nats-io/nats-server/v2

Name:           nats-server
Version:        2.15.1
Release:        %autorelease
Summary:        High-performance cloud-native messaging server
License:        Apache-2.0
URL:            https://github.com/nats-io/nats-server
#!RemoteAsset:  sha256:41b25fcb78a174f3afce4ec1eca0c1035439abf580f0a0569dbb03bd0d955e08
Source0:        https://github.com/nats-io/nats-server/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

BuildOption(build):  -ldflags "-X github.com/nats-io/nats-server/v2/server.serverVersion=%{version}"

BuildRequires:  go >= 1.26.0
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

%check
%go_common
cd %{_builddir}/go/src/%{go_import_path}
%{__go} test -v -vet=off -p=1 -short -timeout=5m -count=1 \
    -run '^TestJetStreamSuperClusterMovingStreamsAndConsumers$/^R1$' ./server

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
