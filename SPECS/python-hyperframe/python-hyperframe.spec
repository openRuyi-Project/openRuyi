# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hyperframe

Name:           python-%{srcname}
Version:        6.1.0
Release:        %autorelease
Summary:        HTTP/2 framing layer for Python
License:        MIT
URL:            https://github.com/python-hyper/hyperframe
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install): %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Pure-Python HTTP/2 framing This library contains the HTTP/2
framing code used in the hyper project. It provides a pure-Python codebase
that is capable of decoding a binary stream into HTTP/2 frames.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%{?autochangelog}
