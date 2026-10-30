# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-caller
%define go_import_path  github.com/newmo-oss/go-caller

Name:           go-github-newmo-oss-go-caller
Version:        0.1.0
Release:        %autorelease
Summary:        Collect stack traces at runtime
License:        MIT
URL:            https://github.com/newmo-oss/go-caller
#!RemoteAsset:  sha256:d1dcb0fda52eec76f20da5020b673cecfdd4ff1ea1eecb0b936fce9ca548325d
Source0:        https://github.com/newmo-oss/go-caller/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The upstream test compares a //line filename with an absolute GOPATH path.
# Normalize it to the injected filename so the test is independent of the OBS build directory.
Patch2000:      2000-tests-compare-line-filenames-by-basename.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp/cmp)

Provides:       go(%{go_import_path}) = %{version}

%description
go-caller collects stack traces at runtime.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
