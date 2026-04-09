# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           bc
Version:        1.08.2
Release:        %autorelease
Summary:        GNU Command Line Calculator
License:        GPL-2.0-or-later
URL:            https://www.gnu.org/software/bc/
# VCS: No VCS link available
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/bc/bc-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/bc/bc-%{version}.tar.gz.sig
BuildSystem:    autotools

BuildRequires:  bison
BuildRequires:  ed
BuildRequires:  flex
BuildRequires:  texinfo

%description
bc is an interpreter that supports numbers of arbitrary precision and
the interactive execution of statements. The syntax has some
similarities to the C programming language. A standard math library is
available through command line options. When used, the math library is
read in before any other input files. bc then reads in all other files
from the command line, evaluating their contents. Then bc reads from
standard input (usually the keyboard).

The dc program is also included. dc is a calculator that supports
reverse-polish notation and allows unlimited precision arithmetic.
Macros can also be defined. Normally, dc reads from standard input but
can also read in files specified on the command line. A calculator with
reverse-polish notation saves numbers to a stack. Arguments to
mathematical operations (operands) are "pushed" onto the stack until
the next operator is read in, which "pops" its arguments off the stack
and "pushes" its results back onto the stack.

%files
%defattr(-,root,root)
%license COPYING.LIB COPYING
%doc NEWS README FAQ
%{_bindir}/bc
%{_bindir}/dc
%{_infodir}/bc.info*
%{_infodir}/dc.info*
%{_mandir}/man1/bc.1*
%{_mandir}/man1/dc.1*

%changelog
%autochangelog
