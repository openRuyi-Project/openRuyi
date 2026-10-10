# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           moby
%define docker_version  29.8.1
%define docker_commit   464cd50c3d9e92877d56940ea160de6fca7bea23
%define api_import_path github.com/moby/moby/api
%define api_version     1.56.0
%define client_import_path github.com/moby/moby/client
%define client_version  0.6.0

Name:           moby
Version:        %{docker_version}
Release:        %autorelease
Summary:        Moby container engine
License:        Apache-2.0
URL:            https://github.com/moby/moby
#!RemoteAsset:  sha256:94be9d6940b613676335fc494e617b4acf98676435b3744f32649ed72114bd58
Source0:        https://github.com/moby/moby/archive/refs/tags/docker-v%{docker_version}.tar.gz#/%{_name}-%{docker_version}.tar.gz
Source1:        moby.sysusers
BuildSystem:    golang

BuildOption(prep):  -n moby-docker-v%{docker_version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go-md2man
BuildRequires:  git
BuildRequires:  make
BuildRequires:  go(github.com/Microsoft/go-winio)
BuildRequires:  go(github.com/containerd/errdefs)
BuildRequires:  go(github.com/containerd/errdefs/pkg)
BuildRequires:  go(github.com/distribution/reference)
BuildRequires:  go(github.com/docker/go-connections)
BuildRequires:  go(github.com/docker/go-units)
BuildRequires:  go(github.com/moby/docker-image-spec)
BuildRequires:  go(github.com/moby/term)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/opencontainers/image-spec)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  systemd-rpm-macros
BuildRequires:  tini-static
BuildRequires:  tzdata

Requires:       containerd >= 2.1.5
Requires:       e2fsprogs
Requires:       iptables-nft
Requires:       procps
Requires:       tini-static
Requires:       xfsprogs
Requires:       xz
Requires(pre):  systemd-sysusers

%description
Moby is an open-source project created by Docker to enable software
containerization. This package provides the Docker daemon (dockerd) and its
userland proxy from the Moby source tree.

%package     -n go-github-moby-moby-api
Version:        %{api_version}
Summary:        Moby Docker Engine API types (source)
BuildArch:      noarch
Provides:       go(%{api_import_path}) = %{api_version}

Requires:       go(github.com/docker/go-units)
Requires:       go(github.com/moby/docker-image-spec)
Requires:       go(github.com/opencontainers/go-digest)
Requires:       go(github.com/opencontainers/image-spec)

%description -n go-github-moby-moby-api
This package provides the versioned Moby Docker Engine API types module used
by Prometheus' Docker and Docker Swarm service discovery.

%package     -n go-github-moby-moby-client
Version:        %{client_version}
Summary:        Moby Docker Engine API client (source)
BuildArch:      noarch
Provides:       go(%{client_import_path}) = %{client_version}

Requires:       go(github.com/Microsoft/go-winio)
Requires:       go(github.com/containerd/errdefs)
Requires:       go(github.com/containerd/errdefs/pkg)
Requires:       go(github.com/distribution/reference)
Requires:       go(github.com/docker/go-connections)
Requires:       go(github.com/docker/go-units)
Requires:       go(%{api_import_path}) = %{api_version}
Requires:       go(github.com/moby/term)
Requires:       go(github.com/opencontainers/go-digest)
Requires:       go(github.com/opencontainers/image-spec)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(golang.org/x/time)

%description -n go-github-moby-moby-client
This package provides the versioned Moby Docker Engine API client module used
by Prometheus' Docker and Docker Swarm service discovery.

%prep -a

%build
# dynbinary produces PIE executables on riscv64; Go requires cgo for PIE.
# This is also Moby's upstream setting for non-static daemon builds.
export CGO_ENABLED=1
export GOTOOLCHAIN=local
export VERSION=%{docker_version}
# Use the commit shown for refs/tags/docker-vX.Y.Z^{} by git ls-remote.
export DOCKER_GITCOMMIT=%{docker_commit}
KEEPDEST=1 KEEPBUNDLE=1 hack/make.sh dynbinary-daemon dynbinary-proxy

%install
install -D -m 0755 bundles/dynbinary-daemon/dockerd %{buildroot}%{_bindir}/dockerd
install -D -m 0755 bundles/dynbinary-proxy/docker-proxy %{buildroot}%{_bindir}/docker-proxy
GO_MD2MAN=%{_bindir}/go-md2man %{__make} -C man prefix=%{_prefix} mandir=%{_mandir} DESTDIR=%{buildroot} install
install -D -m 0644 contrib/init/systemd/docker.service %{buildroot}%{_unitdir}/docker.service
install -D -m 0644 contrib/init/systemd/docker.socket %{buildroot}%{_unitdir}/docker.socket
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/docker.conf
install -d %{buildroot}%{_libexecdir}/docker
ln -s ../../bin/tini-static %{buildroot}%{_libexecdir}/docker/docker-init
rm -rf bundles
install -d %{buildroot}%{go_sys_gopath}/github.com/moby/moby
cp -a api %{buildroot}%{go_sys_gopath}/github.com/moby/moby/api
cp -a client %{buildroot}%{go_sys_gopath}/github.com/moby/moby/client
# Keep importable source and tests, but omit API documentation generators and
# release metadata that are not part of either Go module's compiled surface.
rm -rf %{buildroot}%{go_sys_gopath}/%{api_import_path}/{docs,releases,scripts,templates,validate}
rm -f %{buildroot}%{go_sys_gopath}/%{api_import_path}/{Dockerfile,Makefile,README.md,LICENSE,swagger-gen.yaml,swagger.yaml}
rm -rf %{buildroot}%{go_sys_gopath}/%{client_import_path}/releases
rm -f %{buildroot}%{go_sys_gopath}/%{client_import_path}/{README.md,LICENSE}

%check
%{buildroot}%{_bindir}/dockerd --version
%{buildroot}%{_bindir}/docker-proxy --version
%{_bindir}/tini-static --version
test "$(readlink %{buildroot}%{_libexecdir}/docker/docker-init)" = ../../bin/tini-static
export GOTOOLCHAIN=local
export GOFLAGS="-mod=vendor"
export PATH="%{buildroot}%{_bindir}:$PATH"
go test -vet=off -p=1 \
    -skip "^(TestIfaceAddrs|TestSCTP[46]ProxyNoListener)$" \
    -test.timeout=5m \
    ./cmd/dockerd ./cmd/docker-proxy
# Compile the two source subpackages from the distribution dependency set.
# Their tests import the unshipped full Moby and BuildKit test helpers, so remove
# test files only from this temporary check copy and compile every library package.
unset GOFLAGS
%go_common
install -d %{_builddir}/go/src/github.com/moby/moby
cp -a api %{_builddir}/go/src/github.com/moby/moby/api
cp -a client %{_builddir}/go/src/github.com/moby/moby/client
find %{_builddir}/go/src/github.com/moby/moby -name '*_test.go' -delete
(
    cd %{_builddir}/go/src/github.com/moby/moby
    go test -vet=off ./api/... ./client/...
)

%pre
%sysusers_create_package %{name} %{SOURCE1}

%post
%systemd_post docker.service docker.socket

%preun
%systemd_preun docker.service docker.socket

%postun
%systemd_postun_with_restart docker.service docker.socket

%files
%doc README.md
%license LICENSE NOTICE
%{_bindir}/dockerd
%{_bindir}/docker-proxy
%{_libexecdir}/docker/docker-init
%{_mandir}/man8/dockerd.8*
%{_sysusersdir}/docker.conf
%{_unitdir}/docker.service
%{_unitdir}/docker.socket

%files -n go-github-moby-moby-api
%doc api/README.md
%license api/LICENSE
%{go_sys_gopath}/%{api_import_path}

%files -n go-github-moby-moby-client
%doc client/README.md
%license client/LICENSE
%{go_sys_gopath}/%{client_import_path}

%changelog
%autochangelog
