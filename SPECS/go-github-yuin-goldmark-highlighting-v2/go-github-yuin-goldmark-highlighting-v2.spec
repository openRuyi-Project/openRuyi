# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _name           goldmark-highlighting
%define go_import_path  github.com/yuin/goldmark-highlighting/v2
%global commit_id       37449abec8cc453aad3ea47d44583b172b20f4b1

Name:           go-github-yuin-goldmark-highlighting-v2
Version:        0+git20261023.37449ab
Release:        %autorelease
Summary:        Syntax highlighting extension for Goldmark
License:        MIT
URL:            https://github.com/yuin/goldmark-highlighting
#!RemoteAsset:  sha256:c9b0c8c70313154302cc0413986ea2e2649d93746f56ba84522d352f1fc4de54
Source0:        https://github.com/yuin/goldmark-highlighting/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Refresh HTML and CSS expectations for the distribution Chroma formatter.
Patch2000:      2000-refresh-chroma-rendering-snapshots.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/chroma/v2)
BuildRequires:  go(github.com/yuin/goldmark)

Provides:       go(github.com/yuin/goldmark-highlighting/v2) = %{version}

Requires:       go(github.com/alecthomas/chroma/v2)
Requires:       go(github.com/yuin/goldmark)

%description
Goldmark extension that uses Chroma to highlight fenced code blocks.

%prep
%autosetup -n %{_name}-%{commit_id} -p1

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
