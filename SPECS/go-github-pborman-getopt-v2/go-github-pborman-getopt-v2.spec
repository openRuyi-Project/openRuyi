# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           getopt
%define go_import_path  github.com/pborman/getopt/v2
%define go_source_subdir v2

Name:           go-github-pborman-getopt-v2
Version:        2.1.0
Release:        %autorelease
Summary:        Getopt-style option parsing for Go
License:        BSD-3-Clause
URL:            https://github.com/pborman/getopt
#!RemoteAsset:  sha256:00056fa164b1bf217eb249f5733c76fd6e18f3f55ae269286695705243f48fe2
Source0:        https://github.com/pborman/getopt/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.25 vet rejects non-constant fmt.Fprintf format strings in examples.
# - HNO3Miracle
Patch2000:      2000-fix-non-constant-fprintf-format.patch

# This package owns a Go module below the repository root; the explicit
# %%install/%%check sections below copy only %%{go_source_subdir}, because
# the default golangmodules phases would copy the full archive under
# %%{go_import_path} and create invalid import paths. - HNO3Miracle

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pborman/getopt/v2) = %{version}

%description
Package getopt provides traditional getopt processing for implementing
commands that use traditional command lines.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
export GO111MODULE=off
# Submodule tests may import packages, including internal packages, from the
# parent module. Copy an installed parent tree into the temporary GOPATH first
# so Go's internal package visibility checks use a single physical tree.
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
_go_parent=%{go_import_path}
_go_parent_copy=
while :; do
    _go_next_parent=${_go_parent%/*}
    [ "${_go_next_parent}" = "${_go_parent}" ] && break
    _go_parent=${_go_next_parent}
    if [ -d "%{_datadir}/gocode/src/${_go_parent}" ] &&
       { [ -f "%{_datadir}/gocode/src/${_go_parent}/go.mod" ] ||
         [ -n "$(find "%{_datadir}/gocode/src/${_go_parent}" -maxdepth 1 -name '*.go' -print -quit 2>/dev/null)" ]; }; then
        _go_parent_copy=${_go_parent}
    fi
done
if [ -n "${_go_parent_copy}" ]; then
    mkdir -p "%{_builddir}/go/src/$(dirname "${_go_parent_copy}")"
    rm -rf "%{_builddir}/go/src/${_go_parent_copy}"
    cp -a "%{_datadir}/gocode/src/${_go_parent_copy}" "%{_builddir}/go/src/${_go_parent_copy}"
fi
mkdir -p "%{_builddir}/go/src/$(dirname "%{go_import_path}")"
rm -rf %{_builddir}/go/src/%{go_import_path}
cp -a . %{_builddir}/go/src/%{go_import_path}
cd %{_builddir}/go/src/%{go_import_path}
go test -v $(go list ./...)
popd

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
