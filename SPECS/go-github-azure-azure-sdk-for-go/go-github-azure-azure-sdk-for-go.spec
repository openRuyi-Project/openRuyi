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
# Sub-module versions: Source0..4 are the Prometheus v3.13.1 pins; Source5..6
# are MinIO RELEASE.2025-10-15T17-29-55Z pins (azblob and its go.mod
# armstorage require); Source7..8 are KES 0.24.0 Key Vault dependencies.
# Each maps to an upstream git tag "sdk/<module>/v<ver>"
# in github.com/Azure/azure-sdk-for-go. Maintained by hand; go2spec cannot
# emit a monorepo multi-module spec.
%define ver_azcore      1.22.0
%define ver_azidentity  1.14.0
%define ver_internal    1.12.0
%define ver_armcompute  5.7.0
%define ver_armnetwork  4.3.0
%define ver_azblob      1.6.1
%define ver_armstorage  1.8.0
%define ver_azsecrets    1.1.0
%define ver_kv_internal  1.0.1

# Source archive top-level directory names (github archive layout).
%define dir_azcore      azure-sdk-for-go-sdk-azcore-v%{ver_azcore}
%define dir_azidentity  azure-sdk-for-go-sdk-azidentity-v%{ver_azidentity}
%define dir_internal    azure-sdk-for-go-sdk-internal-v%{ver_internal}
%define dir_armcompute  azure-sdk-for-go-sdk-resourcemanager-compute-armcompute-v%{ver_armcompute}
%define dir_armnetwork  azure-sdk-for-go-sdk-resourcemanager-network-armnetwork-v%{ver_armnetwork}
%define dir_azblob      azure-sdk-for-go-sdk-storage-azblob-v%{ver_azblob}
%define dir_armstorage  azure-sdk-for-go-sdk-resourcemanager-storage-armstorage-v%{ver_armstorage}
%define dir_azsecrets    azure-sdk-for-go-sdk-security-keyvault-azsecrets-v%{ver_azsecrets}
%define dir_kv_internal  azure-sdk-for-go-sdk-security-keyvault-internal-v%{ver_kv_internal}

Name:           go-github-azure-azure-sdk-for-go
Version:        20260615
Release:        %autorelease
Summary:        Azure SDK for Go (core, identity, ARM, storage, Key Vault)
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-go
BuildArch:      noarch
BuildSystem:    golangmodules

# Keep the existing azidentity test-proxy adaptation.
Patch2000:      2000-disable-azidentity-test-proxy.patch
# Run azsecrets offline tests without starting Azure's recording proxy.
Patch2001:      2001-separate-azsecrets-offline-tests.patch

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
#!RemoteAsset:  sha256:77c18709ce1068c40c58e3bcfb4badfa5e041cb915dd86af44407926aaaa8831
Source5:        https://github.com/Azure/azure-sdk-for-go/archive/refs/tags/sdk/storage/azblob/v%{ver_azblob}.tar.gz#/%{_name}-azblob-%{ver_azblob}.tar.gz
#!RemoteAsset:  sha256:ee25b4e734c183d41be74f19150c9c0c92f9d42ddd2c9a276bafae5c2f43b154
Source6:        https://github.com/Azure/azure-sdk-for-go/archive/refs/tags/sdk/resourcemanager/storage/armstorage/v%{ver_armstorage}.tar.gz#/%{_name}-armstorage-%{ver_armstorage}.tar.gz

#!RemoteAsset:  sha256:ffa8c82f223362b4e0ff1d293eae65cfa612535bffdda8d9994c5617e7909bfd
Source7:        https://github.com/Azure/azure-sdk-for-go/archive/refs/tags/sdk/security/keyvault/azsecrets/v%{ver_azsecrets}.tar.gz#/%{_name}-azsecrets-%{ver_azsecrets}.tar.gz
#!RemoteAsset:  sha256:e1138e95e79cdb7680df58360d91c0de5ca16342b95da572501ed3bec1f6c7d6
Source8:        https://github.com/Azure/azure-sdk-for-go/archive/refs/tags/sdk/security/keyvault/internal/v%{ver_kv_internal}.tar.gz#/%{_name}-kv-internal-%{ver_kv_internal}.tar.gz

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
# azblob v%{ver_azblob}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob) = %{ver_azblob}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob/appendblob) = %{ver_azblob}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob/blob) = %{ver_azblob}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob/bloberror) = %{ver_azblob}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob/blockblob) = %{ver_azblob}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob/container) = %{ver_azblob}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob/lease) = %{ver_azblob}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob/pageblob) = %{ver_azblob}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob/sas) = %{ver_azblob}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob/service) = %{ver_azblob}
# armstorage v%{ver_armstorage}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/storage/armstorage) = %{ver_armstorage}

Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/azsecrets) = %{ver_azsecrets}
Provides:       go(github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/internal) = %{ver_kv_internal}

Requires:       go(github.com/AzureAD/microsoft-authentication-library-for-go)
Requires:       go(github.com/golang-jwt/jwt/v5)
Requires:       go(github.com/google/uuid)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/text)

%description
The Azure SDK for Go provides typed clients for Azure services. This
package bundles the sub-modules required by Prometheus' Azure service
discovery (azcore, azidentity, internal, armcompute/v5, armnetwork/v4)
and by MinIO and KES (azblob, armstorage, azsecrets, Key Vault internal).
Each sub-module is installed under its GOPATH import path.

%prep
# Unpack all nine source archives side by side (no merging of trees).
%setup -q -c -T -a 0
%setup -q -D -T -a 1
%setup -q -D -T -a 2
%setup -q -D -T -a 3
%setup -q -D -T -a 4
%setup -q -D -T -a 5
%setup -q -D -T -a 6
%setup -q -D -T -a 7
%setup -q -D -T -a 8
%patch -P 2000 -p1 -d %{dir_azidentity}
%patch -P 2001 -p1 -d %{dir_azsecrets}
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
find %{dir_armstorage}/sdk/resourcemanager/storage/armstorage \
    -name '*_live_test.go' -delete
rm -f %{dir_armstorage}/sdk/resourcemanager/storage/armstorage/utils_test.go
# azblob live tests need sdk/internal/recording as a sibling GOPATH tree
# plus Azure credentials.
find %{dir_azblob}/sdk/storage/azblob -name '*_test.go' -delete
rm -rf %{dir_azblob}/sdk/storage/azblob/testdata
rm -rf %{dir_azblob}/sdk/storage/azblob/internal/testcommon

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
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}/sdk/storage
cp -a %{dir_azblob}/sdk/storage/azblob \
      %{buildroot}%{go_sys_gopath}/%{go_import_path}/sdk/storage/azblob
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}/sdk/resourcemanager/storage
cp -a %{dir_armstorage}/sdk/resourcemanager/storage/armstorage \
      %{buildroot}%{go_sys_gopath}/%{go_import_path}/sdk/resourcemanager/storage/armstorage

install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}/sdk/security/keyvault
cp -a %{dir_azsecrets}/sdk/security/keyvault/azsecrets %{buildroot}%{go_sys_gopath}/%{go_import_path}/sdk/security/keyvault/azsecrets
cp -a %{dir_kv_internal}/sdk/security/keyvault/internal %{buildroot}%{go_sys_gopath}/%{go_import_path}/sdk/security/keyvault/internal

%check
%{go_common}
# Copy every selected module into one GOPATH tree before compiling; azcore and
# azidentity import the independently tagged sdk/internal module.
for mod in \
    sdk/azcore \
    sdk/azidentity \
    sdk/internal \
    sdk/resourcemanager/compute/armcompute/v5 \
    sdk/resourcemanager/network/armnetwork/v4 \
    sdk/resourcemanager/storage/armstorage \
    sdk/storage/azblob \
    sdk/security/keyvault/azsecrets \
    sdk/security/keyvault/internal ; do
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
    sdk/resourcemanager/network/armnetwork/v4 \
    sdk/resourcemanager/storage/armstorage \
    sdk/storage/azblob ; do
  dst="%{_builddir}/go/src/%{go_import_path}/$mod"
  # Compilation must succeed before environment-sensitive tests are tolerated.
  ( cd "$dst" && %__go test -vet=off -run '^$' %{go_test_flags_default} ./... )
  # Some Azure integration tests require credentials, network access or local
  # services unavailable in the isolated build worker.
  ( cd "$dst" && %__go test -vet=off %{go_test_flags_default} ./... ) || :
done

# New Key Vault modules retain vet and fail on any compile or test error.
for mod in sdk/security/keyvault/azsecrets sdk/security/keyvault/internal ; do
  ( cd "%{_builddir}/go/src/%{go_import_path}/$mod" && %__go test %{go_test_flags_default} ./... )
done

%files
%doc %{dir_azcore}/sdk/azcore/README.md
%license %{dir_azcore}/sdk/azcore/LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
