# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           rules_go
%define go_import_path  github.com/bazelbuild/rules_go/go/runfiles

Name:           go-github-bazelbuild-rules-go-go-runfiles
Version:        0.62.0
Release:        %autorelease
Summary:        Bazel runfiles access library for Go
License:        Apache-2.0
URL:            https://github.com/bazelbuild/rules_go
#!RemoteAsset:  sha256:988a8856e5cf6ce5bcb1e30919fe87e444af0fe09ae26ae125035c9522bda147
Source0:        https://github.com/bazelbuild/rules_go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides access to Bazel runfiles from Go programs and tests.

%install
install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}"
cp -a go/runfiles/. "%{buildroot}%{go_sys_gopath}/%{go_import_path}/"

%check
pushd go/runfiles
%buildsystem_golangmodules_check
popd

%files
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
