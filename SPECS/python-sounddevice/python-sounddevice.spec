# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sounddevice

Name:           python-%{srcname}
Version:        0.5.5
Release:        %autorelease
Summary:        Play and Record Sound with Python
License:        MIT
URL:            https://github.com/spatialaudio/python-sounddevice
#!RemoteAsset:  sha256:22487b65198cb5bf2208755105b524f78ad173e5ab6b445bdab1c989f6698df3
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} _%{srcname} -L

BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)

Requires:       portaudio%{?_isa}
Requires:       python3dist(cffi)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
sounddevice provides Python bindings for the PortAudio library, allowing
playback and recording of audio via NumPy arrays. It uses CFFI for the
foreign function interface to PortAudio.

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
