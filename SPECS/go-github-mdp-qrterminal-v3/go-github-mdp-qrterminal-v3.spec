# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           qrterminal
%define go_import_path  github.com/mdp/qrterminal/v3

Name:           go-github-mdp-qrterminal-v3
Version:        3.2.1
Release:        %autorelease
Summary:        A golang library for generating QR codes in the terminal
License:        MIT
URL:            https://github.com/mdp/qrterminal
#!RemoteAsset:  sha256:81ef366cdc8f23f902f9ba35922d8b0f073066a2ebe6dd7989cf1758af7328ac
Source0:        https://github.com/mdp/qrterminal/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(rsc.io/qr)

Provides:       go(github.com/mdp/qrterminal/v3) = %{version}

Requires:       go(github.com/mattn/go-colorable)
Requires:       go(golang.org/x/term)
Requires:       go(rsc.io/qr)

%description
A golang library for generating QR codes in the terminal.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
