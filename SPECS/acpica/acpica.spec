# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xiang W <wangxiang@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           acpica
Version:        20260930
Release:        %autorelease
Summary:        ACPICA tools for the development and debug of ACPI tables
License:        BSD-3-Clause OR GPL-2.0-only
URL:            https://open-acpica.github.io
VCS:            git:https://github.com/open-acpica/acpica.git
#!RemoteAsset:  sha256:aa18901b92e30749be0edc3081c8d550c61fce4fa37546fc6a65d367a4ae71a5
Source0:        https://github.com/open-acpica/acpica/releases/download/%{version}/acpica-unix-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(prep):  -n acpica-unix-%{version}
BuildOption(install):  PREFIX=%{_prefix}

BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  make

%description
ACPICA tools for the development and debug of ACPI tables
 The ACPI Component Architecture (ACPICA) project provides an OS-independent
 reference implementation of the Advanced Configuration and Power Interface
 Specification (ACPI).  ACPICA code contains those portions of ACPI meant to
 be directly integrated into the host OS as a kernel-resident subsystem, and
 a small set of tools to assist in developing and debugging ACPI tables.
 .
 This package contains only the user-space tools needed for ACPI table
 development, not the kernel implementation of ACPI.  The following commands
 are installed:
    -- iasl: compiles ASL (ACPI Source Language) into AML (ACPI Machine
       Language), suitable for inclusion as a DSDT in system firmware.
       It also can disassemble AML, for debugging purposes.
    -- acpibin: performs basic operations on binary AML files (e.g.,
       comparison, data extraction)
    -- acpidump: write out the current contents of ACPI tables
    -- acpiexec: simulate AML execution in order to debug method definitions
    -- acpihelp: display help messages describing ASL keywords and op-codes
    -- acpisrc: manipulate the ACPICA source tree and format source files
       for specific environments
    -- acpixtract: extract binary ACPI tables from acpidump output (see
       also the pmtools package)

# No configure script.
%conf

# No tests.
%check

%files
%license LICENSE.BSD-3-Clause
%license LICENSE.GPL-2.0-only
%{_bindir}/iasl
%{_bindir}/acpixtract
%{_bindir}/acpisrc
%{_bindir}/acpihelp
%{_bindir}/acpiexec
%{_bindir}/acpiexamples
%{_bindir}/acpidump
%{_bindir}/acpibin

%changelog
%autochangelog
