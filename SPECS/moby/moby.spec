# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           moby
%define docker_version  28.5.2
%define docker_commit   89c5e8fd66634b6128fc4c0e6f1236e2540e46e0
# The daemon source uses the v28.5.2 tag. Prometheus v3.12.0/go.mod requires
# github.com/moby/moby/api v1.54.2 and github.com/moby/moby/client v0.4.1;
# their sources use the matching api/v1.54.2 and client/v0.4.1 tags.
%define api_import_path github.com/moby/moby/api
%define api_version     1.54.2
%define api_dir         moby-api-v%{api_version}
%define client_import_path github.com/moby/moby/client
%define client_version  0.4.1
%define client_dir      moby-client-v%{client_version}

# Btrfs and ZFS graphdrivers need optional storage dependencies.
%define docker_buildtags exclude_graphdriver_btrfs exclude_graphdriver_zfs

Name:           moby
Version:        %{docker_version}
Release:        %autorelease
Summary:        Moby container engine
License:        Apache-2.0
URL:            https://github.com/moby/moby
#!RemoteAsset:  sha256:0e450c03c536a1304ba8fd26ca4c4ff96fac62182fd042fec90ffdf4a0969d40
Source0:        https://github.com/moby/moby/archive/refs/tags/v%{docker_version}.tar.gz#/%{_name}-%{docker_version}.tar.gz
#!RemoteAsset:  sha256:f40a40f5b64ef6c7b7734ec08840fef438c1bf96ac29673881a38fb9178f216c
Source1:        https://github.com/moby/moby/archive/refs/tags/api/v%{api_version}.tar.gz#/%{_name}-api-%{api_version}.tar.gz
#!RemoteAsset:  sha256:d10aad65356cd49d0b8c462863253effcc19e18bf7041a9bdb6c1c94097d1280
Source2:        https://github.com/moby/moby/archive/refs/tags/client/v%{client_version}.tar.gz#/%{_name}-client-%{client_version}.tar.gz
Source3:        moby.sysusers
BuildSystem:    golang

# The release tarball extracts to moby-%{docker_version}.
BuildOption(prep):  -n moby-%{docker_version}

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

Provides:       docker = %{version}-%{release}

Requires:       containerd >= 1.7.27
Requires:       e2fsprogs
Requires:       iptables
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
# Prometheus pins the independently tagged Moby API and client modules. Keep
# their source trees beside the Docker program source for the source subpackages.
tar -xzf %{SOURCE1}
tar -xzf %{SOURCE2}

%build
# dynbinary produces PIE executables on riscv64; Go requires cgo for PIE.
# This is also Moby's upstream setting for non-static daemon builds.
export CGO_ENABLED=1
export GOTOOLCHAIN=local
export VERSION=%{docker_version}
# Use the commit shown for refs/tags/vX.Y.Z^{} by git ls-remote.
export DOCKER_GITCOMMIT=%{docker_commit}
export DOCKER_BUILDTAGS="%{docker_buildtags}"
KEEPDEST=1 KEEPBUNDLE=1 hack/make.sh dynbinary-daemon dynbinary-proxy

%install
install -D -m 0755 bundles/dynbinary-daemon/dockerd %{buildroot}%{_bindir}/dockerd
install -D -m 0755 bundles/dynbinary-proxy/docker-proxy %{buildroot}%{_bindir}/docker-proxy
GO_MD2MAN=%{_bindir}/go-md2man %{__make} -C man prefix=%{_prefix} mandir=%{_mandir} DESTDIR=%{buildroot} install
install -D -m 0644 contrib/init/systemd/docker.service %{buildroot}%{_unitdir}/docker.service
install -D -m 0644 contrib/init/systemd/docker.socket %{buildroot}%{_unitdir}/docker.socket
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/docker.conf
install -d %{buildroot}%{_libexecdir}/docker
ln -s ../../bin/tini-static %{buildroot}%{_libexecdir}/docker/docker-init
rm -rf bundles
install -d %{buildroot}%{go_sys_gopath}/github.com/moby/moby
cp -a %{api_dir}/api %{buildroot}%{go_sys_gopath}/github.com/moby/moby/api
cp -a %{client_dir}/client %{buildroot}%{go_sys_gopath}/github.com/moby/moby/client
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
export GOFLAGS="-mod=vendor -modfile=vendor.mod"
export PATH="%{buildroot}%{_bindir}:$PATH"
# Moby uses vendor.mod instead of a root go.mod. Its helper creates a temporary
# go.mod while running the command-package tests, then removes it.
hack/with-go-mod.sh go test -vet=off -p=1 \
    -skip "^(TestIfaceAddrs|TestSCTP[46]ProxyNoListener)$" \
    -tags "%{docker_buildtags}" -test.timeout=5m \
    ./cmd/dockerd ./cmd/docker-proxy
# Compile the two source subpackages from the distribution dependency set.
# Their tests import the unshipped full Moby and BuildKit test helpers, so remove
# test files only from this temporary check copy and compile every library package.
unset GOFLAGS
%go_common
install -d %{_builddir}/go/src/github.com/moby/moby
cp -a %{api_dir}/api %{_builddir}/go/src/github.com/moby/moby/api
cp -a %{client_dir}/client %{_builddir}/go/src/github.com/moby/moby/client
find %{_builddir}/go/src/github.com/moby/moby -name '*_test.go' -delete
(
    cd %{_builddir}/go/src/github.com/moby/moby
    go test -vet=off ./api/... ./client/...
)

%pre
%sysusers_create_package %{name} %{SOURCE3}

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
%doc %{api_dir}/api/README.md
%license %{api_dir}/api/LICENSE
%{go_sys_gopath}/%{api_import_path}

%files -n go-github-moby-moby-client
%doc %{client_dir}/client/README.md
%license %{client_dir}/client/LICENSE
%{go_sys_gopath}/%{client_import_path}

%changelog
%autochangelog
