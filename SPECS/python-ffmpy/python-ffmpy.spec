# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ffmpy

Name:           python-%{srcname}
Version:        1.0.0
Release:        %autorelease
Summary:        Simple Python wrapper for FFmpeg command line utilities
License:        MIT
URL:            https://github.com/Ch00k/ffmpy
VCS:            git:https://github.com/Ch00k/ffmpy.git
#!RemoteAsset:  sha256:b12932e95435c8820f1cd041024402765f821971e4bae753b327fc02a6e12f8b
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# OBS showed modern setuptools rejects several upstream metadata fields during
# %generate_buildrequires. This patch switches to setuptools, preserves package
# discovery, and normalizes only the metadata that hard-fails validation.
Patch0:         2000-python-ffmpy-switch-to-setuptools-build-backend.patch

BuildOption(install):  -l %{srcname} -L
BuildOption(check):    ffmpy

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
ffmpy is a simple Python wrapper for FFmpeg command line utilities such as
ffmpeg and ffprobe.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
