# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           term
%define go_import_path  github.com/charmbracelet/x/term
# The import path is a Go module below the repository root;
# keep %check scopedto this module so GOPATH-mode tests
# do not scan sibling modules from the archive. - HNO3Miracle
%define go_test_include %{go_import_path}

Name:           go-github-charmbracelet-x-term
Version:        0.2.2
Release:        %autorelease
Summary:        Terminal helpers for Go
License:        MIT
URL:            https://github.com/charmbracelet/x
#!RemoteAsset:  sha256:a4fd984c95c538db5063c7cf003d69e93cdc47e5eac6749d75e1594911c651b0
Source0:        https://github.com/charmbracelet/x/archive/refs/tags/term/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/charmbracelet/x/term) = %{version}

Requires:       go(golang.org/x/sys)

%description
This package provides Terminal helpers for Go.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
