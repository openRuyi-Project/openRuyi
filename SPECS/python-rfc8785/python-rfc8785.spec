# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rfc8785

Name:           python-%{srcname}
Version:        0.1.4
Release:        %autorelease
Summary:        Pure Python implementation of RFC 8785 JSON canonicalization
License:        Apache-2.0
URL:            https://github.com/trailofbits/rfc8785.py
VCS:            git:https://github.com/trailofbits/rfc8785.py.git
#!RemoteAsset:  sha256:e545841329fe0eee4f6a3b44e7034343100c12b4ec566dc06ca9735681deb4da
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(flit-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
rfc8785 implements the JSON Canonicalization Scheme described by RFC 8785,
producing deterministic JSON encodings suitable for hashing and signing.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
