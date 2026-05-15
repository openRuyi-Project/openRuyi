# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           msgp
%define go_import_path  github.com/tinylib/msgp
# TODO: Test need too much dependencies, add it later - Julian
%define go_test_exclude %{shrink:
    github.com/tinylib/msgp/msgp
    github.com/tinylib/msgp/tinygotest
}

Name:           go-github-tinylib-msgp
Version:        1.6.4
Release:        %autorelease
Summary:        A Go code generator for MessagePack / msgpack.org
License:        MIT
URL:            https://github.com/tinylib/msgp
#!RemoteAsset:  sha256:1da18b32bb80d663c2a7343987acbde7396253c326f1dc9d52178512e658cb5a
Source0:        https://github.com/tinylib/msgp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

BuildRequires:  go(github.com/philhofer/fwd)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/tinylib/msgp) = %{version}

%description
This is a code generation tool and serialization library for MessagePack. You can read more about MessagePack in the wiki, or at msgpack.org.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
