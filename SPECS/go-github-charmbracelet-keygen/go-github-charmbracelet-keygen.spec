# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           keygen
%define go_import_path  github.com/charmbracelet/keygen

Name:           go-github-charmbracelet-keygen
Version:        0.5.4
Release:        %autorelease
Summary:        An SSH key pair generator 🗝️
License:        MIT
URL:            https://github.com/charmbracelet/keygen
#!RemoteAsset
Source0:        https://github.com/charmbracelet/keygen/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/charmbracelet/keygen) = %{version}

Requires:       go(golang.org/x/crypto)

%description
An SSH key pair generator with password protected keys support. Supports
generating RSA, ECDSA, and Ed25519 keys.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
