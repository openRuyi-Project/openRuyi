# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tokenize-rt
%global modname tokenize_rt

Name:           python-%{srcname}
Version:        6.2.0
Release:        %autorelease
Summary:        Wrapper for Python's stdlib `tokenize` supporting roundtrips
License:        MIT
URL:            https://github.com/asottile/tokenize-rt/
#!RemoteAsset:  sha256:8439c042b330c553fdbe1758e4a05c0ed460dbbbb24a606f11f0dee75da4cad6
Source0:        https://files.pythonhosted.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{modname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The stdlib tokenize module does not properly roundtrip. This wrapper
around the stdlib provides two additional tokens ESCAPED_NL and
UNIMPORTANT_WS, and a Token data type. Use src_to_tokens and
tokens_to_src to roundtrip. This library is useful if you are writing
a refactoring tool based on the python tokenization.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/tokenize-rt

%changelog
%autochangelog
