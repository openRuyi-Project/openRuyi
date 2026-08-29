# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname audioread

Name:           python-%{srcname}
Version:        3.1.0
Release:        %autorelease
Summary:        Multi-library, cross-platform audio decoding in Python
License:        MIT
URL:            https://github.com/beetbox/audioread
#!RemoteAsset:  sha256:1c4ab2f2972764c896a8ac61ac53e261c8d29f0c6ccd652f84e18f08a4cab190
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}
# audioread.macca: macOS specific module
BuildOption(check):  -e 'audioread.macca'
# audioread.maddec: need pymad, which is deprecated on most distributions
BuildOption(check):  -e 'audioread.maddec'

# ffmpeg for test
BuildRequires:  ffmpeg
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pygobject)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Decode audio files using whichever backend is available. Among
currently supports backends are
 o Gstreamer via PyGObject
 o MAD via the pymad bindings
 o FFmpeg or Libav via its command-line interface
 o The standard library wave, aifc, and sunau modules

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
