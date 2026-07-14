# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sof-firmware
Version:        2025.12.2
Release:        %autorelease
Summary:        Firmware and topology files for Sound Open Firmware
License:        Intel-SOF-Firmware-Release-Licence or NXP-SOF-Firmware-Release-Licence
URL:            https://www.sofproject.org/
VCS:            git:https://github.com/thesofproject/sof-bin.git
#!RemoteAsset:  sha256:533f63e3a6d94c09ce05a782657b675fa683ff20787c0979226cf563ec79f517
Source0:        https://github.com/thesofproject/sof-bin/releases/download/v%{version}/sof-bin-%{version}.tar.gz
BuildArch:      noarch

%description
This package contains firmware, topology, and loadable module binaries for
audio devices supported by the Sound Open Firmware project.

%prep
%autosetup -n sof-bin-%{version}

%install
install -d %{buildroot}%{_firmwaredir}/intel
cp -a sof sof-ace-tplg sof-ipc4 sof-ipc4-lib sof-ipc4-tplg sof-tplg %{buildroot}%{_firmwaredir}/intel/

%files
%doc README.md README.Intel manifest.txt sha256sum.txt
%license LICENCE.Intel LICENCE.NXP Notice.NXP
%{_firmwaredir}/intel/sof
%{_firmwaredir}/intel/sof-ace-tplg
%{_firmwaredir}/intel/sof-ipc4
%{_firmwaredir}/intel/sof-ipc4-lib
%{_firmwaredir}/intel/sof-ipc4-tplg
%{_firmwaredir}/intel/sof-tplg

%changelog
%autochangelog
