# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           harmonica
%define go_import_path  github.com/charmbracelet/harmonica

Name:           go-github-charmbracelet-harmonica
Version:        0.2.0
Release:        %autorelease
Summary:        Spring animation library for Go
License:        MIT
URL:            https://github.com/charmbracelet/harmonica
#!RemoteAsset:  sha256:7c6347c3694f28db786d71eed3413a9d65a452a7be93057e65c0994c6dabd45d
Source0:        https://github.com/charmbracelet/harmonica/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/charmbracelet/harmonica) = %{version}

%description
harmonica is a small spring animation library. charmbracelet/bubbles
uses it for physics-based motion.

%prep -a
# examples/ is a nested module of sample programs, not the library.
rm -rf examples

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
