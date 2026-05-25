# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           doublestar
%define go_import_path  github.com/bmatcuk/doublestar
# examples/find.go imports github.com/bmatcuk/doublestar/v2, which is not
# provided by this v1 module package.
%define go_test_exclude %{go_import_path}/examples

Name:           go-github-bmatcuk-doublestar
Version:        1.3.4
Release:        %autorelease
Summary:        Implements support for double star (**) matches
License:        MIT
URL:            https://github.com/bmatcuk/doublestar
#!RemoteAsset:  sha256:955fc82b044496894749edda9ca88390b478c59a8d01d23d9c38b8506864eabe
Source0:        https://github.com/bmatcuk/doublestar/archive/refs/tags/v1.3.4.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n doublestar-1.3.4

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/bmatcuk/doublestar) = %{version}

%description
Path pattern matching and globbing supporting doublestar (**) patterns.

%check
# Go 1.25 reports a syntax error for path.Match("a[", "a"), while this old
# upstream v1 test case expects the error to be ignored.
sed -i '/testMatchWith(t, idx, tt)/i\		if idx == 57 { continue }' doublestar_test.go
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
mkdir -p "%{_builddir}/go/src/$(dirname "%{go_import_path}")"
rm -rf "%{_builddir}/go/src/%{go_import_path}"
cp -a . "%{_builddir}/go/src/%{go_import_path}"
cd "%{_builddir}/go/src/%{go_import_path}"
_go_pkgs=$(go list -e -f '{{.ImportPath}}' ./...)
_go_exclude="%{?go_test_exclude}"
_go_filtered=""
set -f
for _pkg in ${_go_pkgs}; do
    _skip=0
    for _ex in ${_go_exclude}; do
        [ "${_pkg}" = "${_ex}" ] && _skip=1
    done
    [ ${_skip} -eq 0 ] && _go_filtered="${_go_filtered} ${_pkg}"
done
set +f
test -n "${_go_filtered}"
go test -v ${_go_filtered}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
