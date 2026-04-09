# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mapstructure
%define go_import_path  github.com/mitchellh/mapstructure

Name:           go-github-mitchellh-mapstructure
Version:        1.5.0
Release:        %autorelease
Summary:        Go library for decoding generic map values into native Go structures and vice versa.
License:        MIT
URL:            https://github.com/mitchellh/mapstructure
#!RemoteAsset
Source0:        https://github.com/mitchellh/mapstructure/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mitchellh/mapstructure) = %{version}

%description
mapstructure is a Go library for decoding generic map values to
structures and vice versa, while providing helpful error handling.

This library is most useful when decoding values from some data stream
(JSON, Gob, etc.) where you don't *quite* know the structure of the
underlying data until you read a part of it. You can therefore read a
map[string]interface{} and use this library to decode it into the proper
underlying native Go structure.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
