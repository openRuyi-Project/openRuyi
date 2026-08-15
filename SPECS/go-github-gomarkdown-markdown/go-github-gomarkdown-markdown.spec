# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           markdown
%define go_import_path  github.com/gomarkdown/markdown
%define commit_id 8435af3f5984529eff2a2e54ca2ef372c4da2171

Name:           go-github-gomarkdown-markdown
Version:        0+git20260815.8435af3
Release:        %autorelease
Summary:        Markdown parser and HTML renderer for Go
License:        BSD-2-Clause
URL:            https://github.com/gomarkdown/markdown
#!RemoteAsset:  sha256:30c943e65a288cd8bc311b2aead9c843f99f2dc171664d95ed6925e84f741fd0
Source0:        https://github.com/gomarkdown/markdown/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/gomarkdown/markdown) = %{version}

%description
Go library for parsing Markdown text and rendering HTML. It is fast and supports common extensions.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
