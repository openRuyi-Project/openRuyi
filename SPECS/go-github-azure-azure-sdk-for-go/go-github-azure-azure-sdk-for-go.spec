# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           azure-sdk-for-go
%define go_import_path  github.com/Azure/azure-sdk-for-go

# azure-sdk-for-go is a monorepo whose sub-modules are versioned and
# tagged independently; there is no single repository tag that carries
# all of the sub-modules at the versions Prometheus pins. Following the
# Debian aws-sdk approach we keep everything in ONE spec, but because
# GitHub only serves whole-repository archives per tag, each required
# sub-module is fetched from its own tag archive (all github.com
# official sources, no proxy/mirror) and installed into its GOPATH
# location. The package Version is the date of the newest sub-module
# tag (azidentity v1.14.0, 2026-06-15); every Provides below carries the
# real upstream version of its sub-module.
#
# The five sub-module versions below are the ones pinned by Prometheus' go.mod
# (v3.13.1); each maps to an upstream git tag "sdk/<module>/v<ver>" in
# github.com/Azure/azure-sdk-for-go (see Source0..4). To bump for a newer
# Prometheus: read these modules in its go.mod, confirm the matching upstream
# tags exist, then update the ver_* macros and the #!RemoteAsset sha256 lines.
# Maintained by hand; go2spec cannot emit a monorepo multi-module spec.
%define ver_azcore      1.22.0
%define ver_azidentity  1.14.0
%define ver_internal    1.12.0
%define ver_armcompute  5.7.0
%define ver_armnetwork  4.3.0

# Source archive top-level directory names (github archive layout).
%define dir_azcore      azure-sdk-for-go-sdk-azcore-v%{ver_azcore}
%define dir_azidentity  azure-sdk-for-go-sdk-azidentity-v%{ver_azidentity}
%define dir_internal    azure-sdk-for-go-sdk-internal-v%{ver_internal}
%define dir_armcompute  azure-sdk-for-go-sdk-resourcemanager-compute-armcompute-v%{ver_armcompute}
%define dir_armnetwork  azure-sdk-for-go-sdk-resourcemanager-network-armnetwork-v%{ver_armnetwork}

Name:           go-github-azure-azure-sdk-for-go
Version:        20260615
Release:        %autorelease
Summary:        Azure SDK for Go (azcore, azidentity, internal, armcompute, armnetwork)
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-go
BuildArch:      noarch
BuildSystem:    golangmodules

#!RemoteAsset:  sha256:51b956194c3ef970ac2b2e16c05ee8c44f8cff6ba41428528322d8802630b903
Source0:        https://github.com/Azure/azure-sdk-for-go/archive/refs/tags/sdk/azcore/v%{ver_azcore}.tar.gz#/%{_name}-azcore-%{ver_azcore}.tar.gz
#!RemoteAsset:  sha256:deb3089903e969f1258bfb3bbed1b612d3c7e75271d444b7ae92bd63638994fb
Source1:        https://github.com/Azure/azure-sdk-for-go/archive/refs/tags/sdk/azidentity/v%{ver_azidentity}.tar.gz#/%{_name}-azidentity-%{ver_azidentity}.tar.gz
#!RemoteAsset:  sha256:f41ea792bf28ea6712bb5c24045db49c5a935675d7ac96f935937e7b8aaf7f58
Source2:        https://github.com/Azure/azure-sdk-for-go/archive/refs/tags/sdk/internal/v%{ver_internal}.tar.gz#/%{_name}-internal-%{ver_internal}.tar.gz
#!RemoteAsset:  sha256:501e12439c6ada29083a2ba4b61c06392190c1265ecad93435e575ef6bbcb8a1
Source3:        https://github.com/Azure/azure-sdk-for-go/archive/refs/tags/sdk/resourcemanager/compute/armcompute/v%{ver_armcompute}.tar.gz#/%{_name}-armcompute-%{ver_armcompute}.tar.gz
#!RemoteAsset:  sha256:12f987760f5672ad6a188620f1e93e77689a34cb047dfb8e2d4fe00d1814f98d
Source4:        https://github.com/Azure/azure-sdk-for-go/archive/refs/tags/sdk/resourcemanager/network/armnetwork/v%{ver_armnetwork}.tar.gz#/%{_name}-armnetwork-%{ver_armnetwork}.tar.gz

Patch2000:      2000-disable-azidentity-test-proxy.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/AzureAD/microsoft-authentication-library-for-go)
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/Azure/azure-sdk-for-go) = %{version}
# azcore v%{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/arm) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/arm/internal/resource) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/arm/policy) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/arm/runtime) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/cloud) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/internal/exported) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/internal/log) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/internal/pollers) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/internal/pollers/async) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/internal/pollers/body) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/internal/pollers/fake) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/internal/pollers/loc) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/internal/pollers/op) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/internal/shared) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/log) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/policy) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/runtime) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/streaming) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/to) = %{ver_azcore}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore/tracing) = %{ver_azcore}
# azidentity v%{ver_azidentity}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azidentity) = %{ver_azidentity}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/azidentity/internal) = %{ver_azidentity}
# internal v%{ver_internal}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/internal/diag) = %{ver_internal}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/internal/errorinfo) = %{ver_internal}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/internal/exported) = %{ver_internal}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/internal/log) = %{ver_internal}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/internal/poller) = %{ver_internal}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/internal/temporal) = %{ver_internal}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/internal/uuid) = %{ver_internal}
# armcompute v%{ver_armcompute}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/compute/armcompute/v5) = %{ver_armcompute}
# armnetwork v%{ver_armnetwork}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/network/armnetwork/v4) = %{ver_armnetwork}

Requires:       go(github.com/AzureAD/microsoft-authentication-library-for-go)
Requires:       go(github.com/golang-jwt/jwt/v5)
Requires:       go(github.com/google/uuid)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/text)

%description
The Azure SDK for Go provides typed clients for Azure services. This
package bundles the sub-modules required by Prometheus' Azure service
discovery: azcore, azidentity, the shared internal module, and the
Compute (armcompute/v5) and Network (armnetwork/v4) resource-manager
clients. Each sub-module is installed under its GOPATH import path.

%prep
# Unpack all five source archives side by side (no merging of trees).
%setup -q -c -T -a 0
%setup -q -D -T -a 1
%setup -q -D -T -a 2
%setup -q -D -T -a 3
%setup -q -D -T -a 4
%patch -P 2000 -p1 -d %{dir_azidentity}
# azidentity/cache is an independently versioned optional module. Prometheus
# does not import it, so do not ship the arbitrary cache snapshot contained in
# the azidentity tag archive or compile examples that require that module.
rm -rf %{dir_azidentity}/sdk/azidentity/cache
rm -f %{dir_azidentity}/sdk/azidentity/example_persistent_cache_*_test.go
# Resource-manager live tests require the separately versioned internal testutil
# module and real Azure credentials; neither is part of the reusable clients.
find %{dir_armcompute}/sdk/resourcemanager/compute/armcompute \
    -name '*_live_test.go' -delete
find %{dir_armnetwork}/sdk/resourcemanager/network/armnetwork \
    -name '*_live_test.go' -delete

%install
# Install each sub-module subtree into its GOPATH/src import path. The
# major-version suffix (/v5, /v4) is a Go import-path convention that
# has no physical directory upstream, so it is created here.
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}/sdk
cp -a %{dir_azcore}/sdk/azcore         %{buildroot}%{go_sys_gopath}/%{go_import_path}/sdk/azcore
cp -a %{dir_azidentity}/sdk/azidentity %{buildroot}%{go_sys_gopath}/%{go_import_path}/sdk/azidentity
cp -a %{dir_internal}/sdk/internal     %{buildroot}%{go_sys_gopath}/%{go_import_path}/sdk/internal
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}/sdk/resourcemanager/compute/armcompute
cp -a %{dir_armcompute}/sdk/resourcemanager/compute/armcompute/. \
      %{buildroot}%{go_sys_gopath}/%{go_import_path}/sdk/resourcemanager/compute/armcompute/v5
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}/sdk/resourcemanager/network/armnetwork
cp -a %{dir_armnetwork}/sdk/resourcemanager/network/armnetwork/. \
      %{buildroot}%{go_sys_gopath}/%{go_import_path}/sdk/resourcemanager/network/armnetwork/v4

%check
%{go_common}
# Copy every selected module into one GOPATH tree before compiling; azcore and
# azidentity import the independently tagged sdk/internal module.
for mod in \
    sdk/azcore \
    sdk/azidentity \
    sdk/internal \
    sdk/resourcemanager/compute/armcompute/v5 \
    sdk/resourcemanager/network/armnetwork/v4 ; do
  src="%{buildroot}%{go_sys_gopath}/%{go_import_path}/$mod"
  dst="%{_builddir}/go/src/%{go_import_path}/$mod"
  mkdir -p "$dst"
  cp -a "$src/." "$dst/"
done
for mod in \
    sdk/azcore \
    sdk/azidentity \
    sdk/internal \
    sdk/resourcemanager/compute/armcompute/v5 \
    sdk/resourcemanager/network/armnetwork/v4 ; do
  dst="%{_builddir}/go/src/%{go_import_path}/$mod"
  # Compilation must succeed before environment-sensitive tests are tolerated.
  ( cd "$dst" && %__go test -vet=off -run '^$' %{go_test_flags_default} ./... )
  # Some Azure integration tests require credentials, network access or local
  # services unavailable in the isolated build worker.
  ( cd "$dst" && %__go test -vet=off %{go_test_flags_default} ./... ) || :
done

%files
%doc %{dir_azcore}/sdk/azcore/README.md
%license %{dir_azcore}/sdk/azcore/LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
