# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nibabel

Name:           python-%{srcname}
Version:        5.3.3
Release:        %autorelease
Summary:        Python package to access a cacophony of neuro-imaging file formats
License:        MIT AND PDDL-1.0
URL:            http://nipy.org/nibabel/
VCS:            git:https://github.com/nipy/nibabel
#!RemoteAsset:  sha256:8d2006b70d727fd0a798a88ae5fd64339741f436fcfc83d6ea3256cdbc51c5b7
Source:         https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(numpy)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
This package provides read +/- write access to some common medical and
neuroimaging file formats, including: ANALYZE, GIFTI, NIfTI1, NIfTI2, MINC1,
MINC2, MGH and ECAT as well as Philips PAR/REC.

%generate_buildrequires
%pyproject_buildrequires

%check
# skip tests as some deps we don't have yet.

%files -f %{pyproject_files}
%license COPYING
%doc README.rst
%{_bindir}/parrec2nii
%{_bindir}/nib-*

%changelog
%{?autochangelog}
