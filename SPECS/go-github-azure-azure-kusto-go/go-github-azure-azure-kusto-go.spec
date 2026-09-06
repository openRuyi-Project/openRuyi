# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           azure-kusto-go
%define go_import_path  github.com/Azure/azure-kusto-go
# Root tests assert host DNS error text, which differs in the OBS network.
# End-to-end tests require external Azure services and a private config file.
%define go_test_exclude %{go_import_path}/azkustodata %{go_import_path}/azkustodata/test/etoe

Name:           go-github-azure-azure-kusto-go
Version:        1.2.2
Release:        %autorelease
Summary:        Azure Data Explorer client library for Go
License:        MIT
URL:            https://github.com/Azure/azure-kusto-go
#!RemoteAsset:  sha256:96dadcebea19e69dc417755551ab7683095702971b68e070083887a74011ed0a
Source0:        https://github.com/Azure/azure-kusto-go/archive/refs/tags/azkustodata/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-azkustodata-v%{version}

# Use a constant format string for the quickstart ingestion error.
Patch2000:      2000-fix-quickstart-ingestion-error-formatting.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azcore)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azidentity)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/data/aztables)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/internal/diag)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/storage/azqueue)
BuildRequires:  go(github.com/AzureAD/microsoft-authentication-library-for-go)
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/gofrs/uuid)
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/kylelemons/godebug)
BuildRequires:  go(github.com/pkg/browser)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/samber/lo)
BuildRequires:  go(github.com/shopspring/decimal)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tj/assert)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/azidentity)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/data/aztables)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/storage/azqueue)
Requires:       go(github.com/cenkalti/backoff/v4)
Requires:       go(github.com/gofrs/uuid)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/kylelemons/godebug)
Requires:       go(github.com/samber/lo)
Requires:       go(github.com/shopspring/decimal)

%description
Azure Kusto Go provides data query and ingestion clients for Azure Data
Explorer. This package installs all modules from the upstream repository.

%install
install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}"
cp -a ./. "%{buildroot}%{go_sys_gopath}/%{go_import_path}/"

%check
export GO111MODULE=off
export GODEBUG=asynctimerchan=0
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
install -d "%{_builddir}/go/src/%{go_import_path}"
cp -a ./. "%{_builddir}/go/src/%{go_import_path}/"
pushd "%{_builddir}/go/src/%{go_import_path}"
while IFS= read -r -d '' _go_mod; do
    _module_dir=${_go_mod%/go.mod}
    pushd "${_module_dir}"
    _go_pkgs=$(go list -e -f '{{.ImportPath}}' ./...)
    _go_test_pkgs=
    for _go_pkg in ${_go_pkgs}; do
        case " %{go_test_exclude} " in
            *" ${_go_pkg} "*) go test -run '^$' "${_go_pkg}" ;;
            *) _go_test_pkgs="${_go_test_pkgs} ${_go_pkg}" ;;
        esac
    done
    if [ -n "${_go_test_pkgs}" ]; then
        go test -v ${_go_test_pkgs}
    fi
    popd
done < <(find . -name go.mod -print0 | sort -z)
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
