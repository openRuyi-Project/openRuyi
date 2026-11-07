# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pywavelets

Name:           python-%{srcname}
Version:        1.9.0
Release:        %autorelease
Summary:        PyWavelets, wavelet transform module
License:        MIT AND BSD-3-Clause
URL:            https://github.com/PyWavelets/pywt
#!RemoteAsset:  sha256:148d12203377772bea452a59211d98649c8ee4a05eff019a9021853a36babdc8
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l pywt
# These fixture generators require proprietary MATLAB and pymatbridge.
BuildOption(check):  -e 'pywt.tests.data.generate_matlab_data*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PyWavelets provides discrete and continuous wavelet transforms, wavelet
packets, and multidimensional signal decomposition and reconstruction.

%generate_buildrequires
%pyproject_buildrequires -p

%files -f %{pyproject_files}

%changelog
%autochangelog
