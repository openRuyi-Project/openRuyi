# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Exclude errors for dependencies ending in sh, for example ash, pdksh and so on.
%define __requires_exclude sh$

Name:           parallel
Version:        20250822
Release:        %autorelease
Summary:        Shell tool for executing jobs in parallel
License:        GPL-3.0-or-later AND GFDL-1.3-or-later
URL:            https://www.gnu.org/software/parallel/
VCS:            git:https://https.git.savannah.gnu.org/git/parallel.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  sed
# bash-completion for %%{bash_completions_dir}
BuildRequires:  bash-completion

%description
GNU Parallel is a shell tool for executing jobs in parallel using one or more
machines. A job is typically a single command or a small script that has to be
run for each of the lines in the input.

%conf -p
autoreconf -ivf

%files
%license LICENSES/GPL-3.0-or-later.txt LICENSES/GFDL-1.3-or-later.txt
%doc %{_docdir}/%{name}
%doc README NEWS
%{_bindir}/parallel
%{_bindir}/parcat
%{_bindir}/parset
%{_bindir}/parsort
%{_bindir}/env_parallel*
%{_bindir}/sem
%{_bindir}/sql
%{_bindir}/niceload
%{_mandir}/man1/parallel.1*
%{_mandir}/man1/parcat.1*
%{_mandir}/man1/parset.1*
%{_mandir}/man1/parsort.1*
%{_mandir}/man1/env_parallel.1*
%{_mandir}/man1/sem.1*
%{_mandir}/man1/sql.1*
%{_mandir}/man1/niceload.1*
%{_mandir}/man7/parallel*
%{_datadir}/bash-completion/completions/parallel
%{_datadir}/zsh/site-functions/_parallel

%changelog
%autochangelog
