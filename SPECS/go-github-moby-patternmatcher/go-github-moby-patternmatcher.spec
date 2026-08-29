# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           patternmatcher
%define go_import_path  github.com/moby/patternmatcher

Name:           go-github-moby-patternmatcher
Version:        0.6.1
Release:        %autorelease
Summary:        Docker-style ignore-pattern matching for Go
License:        Apache-2.0
URL:            https://github.com/moby/patternmatcher
#!RemoteAsset:  sha256:9c32428a3338eb7bd102ad68f9e3b7be21c75fd62400b0cadf2f125cc3e4243a
Source0:        https://github.com/moby/patternmatcher/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/moby/patternmatcher) = %{version}

%description
patternmatcher implements Docker-style pattern matching (.dockerignore semantics) for Go.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
