# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gcp
%define go_import_path  github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp
%define go_source_subdir detectors/gcp
# This tag archive is the repository root; keep %check scoped to this module
# so GOPATH-mode tests do not scan sibling modules from the archive. - HNO3Miracle
%define go_test_include %{go_import_path}

Name:           go-github-googlecloudplatform-opentelemetry-operations-go-detectors-gcp
Version:        1.32.0
Release:        %autorelease
Summary:        GCP resource detector for OpenTelemetry
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/opentelemetry-operations-go
#!RemoteAsset:  sha256:1854804e4ae88e377cc847ab34d999a4501ca2754dd92b86729e4469f2db6f8b
Source0:        https://github.com/GoogleCloudPlatform/opentelemetry-operations-go/archive/refs/tags/detectors/gcp/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp) = %{version}

Requires:       go(cloud.google.com/go/compute/metadata)

%description
This package provides the GCP resource detector for OpenTelemetry.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
mkdir -p "%{_builddir}/go/src/$(dirname "%{go_import_path}")"
rm -rf "%{_builddir}/go/src/%{go_import_path}"
cp -a . "%{_builddir}/go/src/%{go_import_path}"
cd "%{_builddir}/go/src/%{go_import_path}"
_go_pkgs="%{?go_test_include}"
if [ -z "${_go_pkgs}" ]; then
    _go_pkgs=$(go list -e -f '{{.ImportPath}}' ./...)
fi
_go_exclude="%{?go_test_exclude}"
_go_exclude_glob="%{?go_test_exclude_glob}"
_go_filtered=""
set -f
for _pkg in ${_go_pkgs}; do
    _skip=0
    for _ex in ${_go_exclude}; do
        [ "${_pkg}" = "${_ex}" ] && _skip=1
    done
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
%doc detectors/gcp/README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
