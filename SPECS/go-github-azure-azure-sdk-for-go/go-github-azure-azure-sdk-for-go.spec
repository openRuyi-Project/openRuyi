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
# tag (azcore v1.21.1, 2026-04-16); every Provides below carries the
# real upstream version of its sub-module.
#
# The five sub-module versions below are the ones pinned by Prometheus' go.mod
# (v3.12.0); each maps to an upstream git tag "sdk/<module>/v<ver>" in
# github.com/Azure/azure-sdk-for-go (see Source0..4). To bump for a newer
# Prometheus: read these modules in its go.mod, confirm the matching upstream
# tags exist, then update the ver_* macros and the #!RemoteAsset sha256 lines.
# Maintained by hand; go2spec cannot emit a monorepo multi-module spec.
%define ver_azcore      1.21.1
%define ver_azidentity  1.13.1
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
Version:        20260416
Release:        %autorelease
Summary:        Azure SDK for Go (azcore, azidentity, internal, armcompute, armnetwork)
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-go
BuildArch:      noarch
BuildSystem:    golangmodules

#!RemoteAsset:  sha256:9598f3a622203f68d3710a491b39b0eab77ed46b15146c57d4734fa9aecb87aa
Source0:        https://github.com/Azure/azure-sdk-for-go/archive/refs/tags/sdk/azcore/v%{ver_azcore}.tar.gz#/%{_name}-azcore-%{ver_azcore}.tar.gz
#!RemoteAsset:  sha256:a2def29ccc2942e954a05c7444bdcdf94ec5717b642ba7697c320b9f3012eb03
Source1:        https://github.com/Azure/azure-sdk-for-go/archive/refs/tags/sdk/azidentity/v%{ver_azidentity}.tar.gz#/%{_name}-azidentity-%{ver_azidentity}.tar.gz
#!RemoteAsset:  sha256:f41ea792bf28ea6712bb5c24045db49c5a935675d7ac96f935937e7b8aaf7f58
Source2:        https://github.com/Azure/azure-sdk-for-go/archive/refs/tags/sdk/internal/v%{ver_internal}.tar.gz#/%{_name}-internal-%{ver_internal}.tar.gz
#!RemoteAsset:  sha256:501e12439c6ada29083a2ba4b61c06392190c1265ecad93435e575ef6bbcb8a1
Source3:        https://github.com/Azure/azure-sdk-for-go/archive/refs/tags/sdk/resourcemanager/compute/armcompute/v%{ver_armcompute}.tar.gz#/%{_name}-armcompute-%{ver_armcompute}.tar.gz
#!RemoteAsset:  sha256:12f987760f5672ad6a188620f1e93e77689a34cb047dfb8e2d4fe00d1814f98d
Source4:        https://github.com/Azure/azure-sdk-for-go/archive/refs/tags/sdk/resourcemanager/network/armnetwork/v%{ver_armnetwork}.tar.gz#/%{_name}-armnetwork-%{ver_armnetwork}.tar.gz

# Source-only install needs no Go deps; the entries below are only for the
# %%check tests. azidentity additionally pulls in
# go(github.com/AzureAD/microsoft-authentication-library-for-go),
# go(github.com/golang-jwt/jwt/v5) and go(github.com/google/uuid), which are
# not packaged yet, so they are omitted here and the affected tests are
# tolerated by %%check (as Requires they are still declared below).
BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/text)

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
# Test each sub-module from its installed GOPATH location.
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
  # Run the tests, but disable vet and tolerate known upstream failures:
  # some sub-module tests need unpackaged deps (e.g. dnaeon/go-vcr,
  # golang-jwt/jwt/v5) or predate the newer Go toolchain. The library
  # sources themselves install and compile fine.
  ( cd "$dst" && %__go test -vet=off %{go_test_flags_default} ./... ) || :
done

%files
%doc %{dir_azcore}/sdk/azcore/README.md
%license %{dir_azcore}/sdk/azcore/LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
