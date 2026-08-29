# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           metadata
%define go_import_path  cloud.google.com/go/compute/metadata
%define go_source_subdir compute/metadata

Name:           go-googlecloud-go-compute-metadata
Version:        0.9.0
Release:        %autorelease
Summary:        Google Compute metadata client for Go
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-go
#!RemoteAsset:  sha256:6c91b83e40f93b7a9e07d41bf06fe615a9a4498f6aaa6e8e32328231b9c260b3
Source0:        https://github.com/googleapis/google-cloud-go/archive/refs/tags/compute/metadata/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The explicit %%install/%%check sections below enter %%{go_source_subdir};
# otherwise this package would install the whole google-cloud-go repository and
# conflict with sibling cloud.google.com/go submodules. - HNO3Miracle

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(cloud.google.com/go/compute/metadata) = %{version}

%description
This package provides a Go client for the Google Compute metadata service.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
%buildsystem_golangmodules_check
popd

%files
%doc %{go_source_subdir}/CHANGES.md
%doc %{go_source_subdir}/README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
