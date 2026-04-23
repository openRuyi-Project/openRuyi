# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pydub

Name:           python-%{srcname}
Version:        0.25.1
Release:        %autorelease
Summary:        Audio manipulation with Python
License:        MIT
URL:            https://github.com/jiaaro/pydub
#!RemoteAsset:  sha256:980a33ce9949cab2a569606b65674d748ecbca4f0796887fd6f46173a7b0d30f
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# gh#jiaaro/pydub#700 mcepl@suse.com
Patch0:         0001-skip_libopenh264-7.patch
# gh#jiaaro/pydub#769
Patch1:         0002-fix-assertions.patch

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A Python module to manipulate audio with a high level interface.

%generate_buildrequires
%pyproject_buildrequires

# No module named 'pyaudioop'
# No module named 'audioop'
%check

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
