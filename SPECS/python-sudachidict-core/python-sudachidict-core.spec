# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sudachidict-core
%global pypi_name sudachidict_core

Name:           python-%{srcname}
Version:        20260116
Release:        %autorelease
Summary:        A lexicon for Sudachi
License:        Apache-2.0
URL:            https://github.com/WorksApplications/SudachiDict
#!RemoteAsset:  sha256:81d3c8bbd880a58de33f9fb441663f46fb46a97b829d7ba7598f7085fedf319e
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:e74b86d76fd07bfb162aee45f52c57958a4abc1f627ec0013327a64202362499
Source1:        http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict-raw/%{version}/core_lex.zip
#!RemoteAsset:  sha256:0ad4a03a55ae1f71cd86be615c38b93a649ee7f9a089a1ac9049ea1829586c6d
Source2:        http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict-raw/%{version}/small_lex.zip
#!RemoteAsset:  sha256:3ccaed582481b31be170c7200cf1cb2856f2d14c2fa601b3692d97dbad5a3bd1
Source3:        http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict-raw/matrix.def.zip
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(sudachipy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  unzip

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A lexicon for Japanese tokenizer Sudachi.

%generate_buildrequires
%pyproject_buildrequires

%prep -a
mkdir -p sudachidict_core/resources
unzip -j %{SOURCE1} -d .
unzip -j %{SOURCE2} -d .
unzip -j %{SOURCE3} -d .

%build -p
sudachipy build -o sudachidict_core/resources/system.dic -d "Built for openRuyi" -m matrix.def core_lex.csv small_lex.csv

%files -f %{pyproject_files}
%doc README.md
%license LICENSE-2.0.txt

%changelog
%autochangelog
