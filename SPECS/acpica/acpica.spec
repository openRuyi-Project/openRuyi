# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xiang W <wangxiang@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           acpica
Version:        20251212
Release:        %autorelease
Summary:        ACPICA tools for the development and debug of ACPI tables
License:        GPL-2.0-only
URL:            https://www.acpica.org
VCS:            git:https://github.com/acpica/acpica
#!RemoteAsset:  sha256:6f77bd550655183c63f0a307fb0f29ef6140b1f522d61783a16b2af8d9149a0d
Source0:        https://github.com/acpica/acpica/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

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
%{_bindir}/iasl
%{_bindir}/acpixtract
%{_bindir}/acpisrc
%{_bindir}/acpihelp
%{_bindir}/acpiexec
%{_bindir}/acpiexamples
%{_bindir}/acpidump
%{_bindir}/acpibin

%changelog
%{?autochangelog}
