# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname librosa

Name:           python-%{srcname}
Version:        1.0.0
Release:        %autorelease
Summary:        Python module for audio and music processing
License:        ISC
URL:            https://github.com/librosa/librosa
#!RemoteAsset:  sha256:73ed480d4022e436e85dfa6f6b06ff38a259b9210039ac99939cd64854b61a57
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(matplotlib)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Librosa provides algorithms for music and audio signal processing, including
spectral analysis, feature extraction, and time-frequency transformations.

%generate_buildrequires
%pyproject_buildrequires

%check -p
# Keep Numba import-time JIT caches outside the installed Python module tree.
export NUMBA_CACHE_DIR=%{_builddir}/numba-cache

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
