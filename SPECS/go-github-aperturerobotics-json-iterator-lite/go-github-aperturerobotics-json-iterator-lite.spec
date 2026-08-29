# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           json-iterator-lite
%define go_import_path  github.com/aperturerobotics/json-iterator-lite

Name:           go-github-aperturerobotics-json-iterator-lite
Version:        1.1.0
Release:        %autorelease
Summary:        Implements encoding and decoding of JSON as defined in RFC 4627 and provides interfaces with identical syntax of standard lib encoding/json
License:        MIT
URL:            https://github.com/aperturerobotics/json-iterator-lite
#!RemoteAsset:  sha256:00ab7e168d96f2cb925debddf7a94b1ee2db322c33e347ad50b929202eb9fea7
Source0:        https://github.com/aperturerobotics/json-iterator-lite/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/aperturerobotics/json-iterator-lite) = %{version}

%description
json-iterator is an alternative to encoding/json which does not
use reflection.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
