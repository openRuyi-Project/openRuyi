# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname standard-aifc
%global pypi_name standard_aifc

Name:           python-%{srcname}
Version:        3.13.0
Release:        %autorelease
Summary:        Read and write audio files in AIFF or AIFC format
License:        PSF-2.0
URL:            https://github.com/youknowone/python-deadlib
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  aifc

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This module provides support for reading and writing AIFF and AIFF-C files. AIFF
is Audio Interchange File Format, a format for storing digital audio samples in a
file. AIFF-C is a newer version of the format that includes the ability to compress
the audio data.

Audio files have a number of parameters that describe the audio data. The sampling
rate or frame rate is the number of times per second the sound is sampled. The number
of channels indicate if the audio is mono, stereo, or quadro. Each frame consists of
one sample per channel. The sample size is the size in bytes of each sample. Thus a
frame consists of nchannels * samplesize bytes, and a second's worth of audio consists
of nchannels * samplesize * framerate bytes.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
