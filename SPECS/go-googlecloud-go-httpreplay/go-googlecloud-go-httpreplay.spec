# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           httpreplay
%define go_import_path  cloud.google.com/go/httpreplay
%define go_source_subdir httpreplay
# Root tests import cloud.google.com/go/storage, while storage BuildRequires
# this package. Keep internal proxy tests but exclude root and cmd/httpr to
# avoid the bootstrap cycle. - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    %{go_import_path}
    %{go_import_path}/cmd/httpr
}

Name:           go-googlecloud-go-httpreplay
Version:        1.62.2
Release:        %autorelease
Summary:        HTTP replay helpers for Google Cloud Go tests
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-go
#!RemoteAsset:  sha256:38afa699c95151053154d1ab2605148a05768e41ade567c6dc15920562893a79
Source0:        https://github.com/googleapis/google-cloud-go/archive/refs/tags/storage/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cloud.google.com/go/internal)
BuildRequires:  go(github.com/google/martian/v3)
BuildRequires:  go(google.golang.org/api)

Provides:       go(cloud.google.com/go/httpreplay) = %{version}

Requires:       go(cloud.google.com/go/internal)
Requires:       go(github.com/google/martian/v3)
Requires:       go(google.golang.org/api)

%description
This package provides HTTP record/replay helpers used by Google Cloud Go tests.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
rm -rf "%{_builddir}/go/src/cloud.google.com/go"
mkdir -p "%{_builddir}/go/src/$(dirname "%{go_import_path}")"
cp -a . "%{_builddir}/go/src/%{go_import_path}"
cp -a ../internal "%{_builddir}/go/src/cloud.google.com/go/internal"
cd "%{_builddir}/go/src/%{go_import_path}"
# cmd/httpr/integration_test.go imports cloud.google.com/go/storage; storage
# BuildRequires this package, so skip that command package to avoid the same
# bootstrap cycle while still running the local proxy tests. - HNO3Miracle
_go_pkgs=$(go list -e -f '{{.ImportPath}}' ./...)
_go_exclude_glob="%{?go_test_exclude_glob}"
_go_filtered=""
set -f
for _pkg in ${_go_pkgs}; do
    _skip=0
    for _ex in ${_go_exclude_glob}; do
        case "${_pkg}" in ${_ex}) _skip=1 ;; esac
    done
    [ ${_skip} -eq 0 ] && _go_filtered="${_go_filtered} ${_pkg}"
done
set +f
test -n "${_go_filtered}"
go test -v ${_go_filtered}
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
