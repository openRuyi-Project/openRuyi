# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           circbuf
%define go_import_path  github.com/armon/circbuf
%define commit_id 5111143e8da2e98b4ea6a8f32b9065ea1821c191

Name:           go-github-armon-circbuf
Version:        0+git20190214.5111143
Release:        %autorelease
Summary:        Golang circular (ring) buffer
License:        MIT
URL:            https://github.com/armon/circbuf
#!RemoteAsset
Source0:        https://github.com/armon/circbuf/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/armon/circbuf) = %{version}

%description
This repository provides the circbuf package. This provides a Buffer
object which is a circular (or ring) buffer. It has a fixed size, but
can be written to infinitely. Only the last size bytes are ever
retained. The buffer implements the io.Writer interface.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
