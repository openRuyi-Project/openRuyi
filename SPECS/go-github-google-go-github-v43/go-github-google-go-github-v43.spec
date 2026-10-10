# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-github
%define go_import_path  github.com/google/go-github/v43

Name:           go-github-google-go-github-v43
Version:        43.0.0
Release:        %autorelease
Summary:        Go client library for the GitHub API
License:        BSD-3-Clause
URL:            https://github.com/google/go-github
#!RemoteAsset:  sha256:78baf73614ebefd56f822c7c9a0d60793c561acca9402e8d2a2d18190b905cba
Source0:        https://github.com/google/go-github/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Use the bundled v43 root module for the bundled scrape module.
Patch2000:      2000-Use-bundled-root-module-in-scrape-package.patch
# Fix a non-constant format string rejected by current Go vet.
Patch2001:      2001-Fix-non-constant-update-urls-test-format-string.patch

BuildRequires:  go
BuildRequires:  go(github.com/GoKillers/libsodium-go)
BuildRequires:  go(github.com/PuerkitoBio/goquery)
BuildRequires:  go(github.com/bradleyfalzon/ghinstallation/v2)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-querystring)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/xlzd/gotp)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(google.golang.org/appengine)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/google/go-github/scrape) = %{version}
Provides:       go(github.com/google/go-github/update-urls) = %{version}
Provides:       go(github.com/google/go-github/v43) = %{version}
Provides:       go(github.com/google/go-github/v43/example/appengine) = %{version}
Provides:       go(github.com/google/go-github/v43/github) = %{version}
Provides:       go(github.com/google/go-github/v43/test/integration) = %{version}

Requires:       go(github.com/GoKillers/libsodium-go)
Requires:       go(github.com/PuerkitoBio/goquery)
Requires:       go(github.com/bradleyfalzon/ghinstallation/v2)
Requires:       go(github.com/google/go-querystring)
Requires:       go(github.com/xlzd/gotp)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(google.golang.org/appengine)

%description
Go-github provides a Go client library for accessing the GitHub REST API.

%install
# Install each module at its declared import path. Remove nested module
# copies from each parent before installing them at their own paths.
while read -r _source _import _children; do
    _target="%{buildroot}%{go_sys_gopath}/${_import}"
    install -d "${_target}"
    cp -aL "${_source}"/. "${_target}/"
    for _child in ${_children}; do
        rm -rf "${_target}/${_child}"
    done
done <<'GO_MODULES'
. github.com/google/go-github/v43 scrape update-urls
scrape github.com/google/go-github/scrape
update-urls github.com/google/go-github/update-urls
GO_MODULES

%check
%go_common
# Test the installed layout, including nested modules, without loading a
# second copy of the repository or using the system's older source package.
install -d "%{_builddir}/go/src"
cp -a "%{buildroot}%{go_sys_gopath}/." "%{_builddir}/go/src/"
_go_packages=$(go list -e -f '{{.ImportPath}}' github.com/google/go-github/...)
_go_packages=$(printf '%s\n' "${_go_packages}" | sort -u)
_go_tests=
set -f
for _package in ${_go_packages}; do
    _skip=0
    for _exclude in %{?go_test_exclude}; do
        if [ "${_package}" = "${_exclude}" ]; then _skip=1; fi
    done
    for _exclude in %{?go_test_exclude_glob}; do
        case "${_package}" in ${_exclude}) _skip=1 ;; esac
    done
    [ "${_skip}" -eq 1 ] || _go_tests="${_go_tests} ${_package}"
done
set +f
test -n "${_go_tests}"
go test %{go_test_flags_default} ${_go_tests}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%{go_sys_gopath}/github.com/google/go-github/scrape
%{go_sys_gopath}/github.com/google/go-github/update-urls

%changelog
%autochangelog
