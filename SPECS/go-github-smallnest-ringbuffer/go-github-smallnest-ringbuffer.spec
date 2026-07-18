# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ringbuffer
%define go_import_path  github.com/smallnest/ringbuffer

Name:           go-github-smallnest-ringbuffer
Version:        0.1.1
Release:        %autorelease
Summary:        A circular buffer (ring buffer) in Go, implemented io.ReaderWriter interface
License:        MIT
URL:            https://github.com/smallnest/ringbuffer
#!RemoteAsset:  sha256:ac3e832e1cb9c90c3d070e091656215df3c67cf074fbe87bd3b4b2bc5c4f5e55
Source0:        https://github.com/smallnest/ringbuffer/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/smallnest/ringbuffer) = %{version}

%description
A circular buffer (ring buffer) in Go, implemented io.ReaderWriter
interface

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
