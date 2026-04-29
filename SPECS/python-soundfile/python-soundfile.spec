# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname soundfile

Name:           python-%{srcname}
Version:        0.13.1
Release:        %autorelease
Summary:        An audio library based on libsndfile, CFFI and NumPy
License:        BSD-3-Clause
URL:            https://github.com/bastibe/python-soundfile
VCS:            git:https://github.com/bastibe/python-soundfile.git
#!RemoteAsset:  sha256:b2c68dab1e30297317080a5b43df57e302584c49e2942defdde0acccc53f0e5b
Source:         https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} _soundfile

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(setuptools)

Requires:       python3dist(cffi)
Requires:       python3dist(numpy)
Requires:       libsndfile

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
python-soundfile is an audio library based on libsndfile, CFFI and NumPy.
Full documentation is available on https://python-soundfile.readthedocs.io/.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
