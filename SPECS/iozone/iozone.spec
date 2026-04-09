# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           iozone
Version:        3_508
Release:        %autorelease
Summary:        Iozone Filesystem Benchmark
License:        GPL-2.0-or-later
URL:            http://www.iozone.org/
# VCS: No VCS link available
#!RemoteAsset
Source0:        http://www.iozone.org/src/current/%{name}%{version}.tar

BuildRequires:  make
BuildRequires:  libtool

%description
IOzone is a filesystem benchmark tool. The benchmark generates and
measures a variety of file operations. Iozone has been ported to many machines and runs under many operating systems.

Iozone is useful for performing a broad filesystem analysis of a vendors
computer platform. The benchmark tests file I/O performance for the following
operations:     Read, write, re-read, re-write, read backwards, read strided,
fread, fwrite, random read, pread ,mmap, aio_read, aio_write.

%prep
%autosetup -n iozone%{version}/src/current

%build
%ifarch x86_64
make linux-AMD64
%endif

%ifarch riscv64
make linux
%endif

%install
# no make install
install -Dm755 iozone %{buildroot}%{_bindir}/iozone
install -Dm755 fileop %{buildroot}%{_bindir}/fileop
install -Dm755 pit_server %{buildroot}%{_bindir}/pit_server
install -Dm755 Generate_Graphs %{buildroot}%{_bindir}/Generate_Graphs
install -Dm755 gengnuplot.sh %{buildroot}%{_bindir}/gengnuplot.sh
install -Dm644 gnu3d.dem %{buildroot}%{_bindir}/gnu3d.dem

install -Dm644 $RPM_BUILD_DIR/iozone%{version}/docs/IOzone_msword_98.pdf %{buildroot}%{_docdir}/iozone/IOzone_msword_98.pdf
install -Dm644 $RPM_BUILD_DIR/iozone%{version}/docs/Run_rules.doc %{buildroot}%{_docdir}/iozone/Run_rules.doc
install -Dm644 $RPM_BUILD_DIR/iozone%{version}/docs/IOzone_msword_98.doc %{buildroot}%{_docdir}/iozone/IOzone_msword_98.doc
install -Dm644 $RPM_BUILD_DIR/iozone%{version}/docs/Iozone_ps.gz %{buildroot}%{_docdir}/iozone/Iozone_ps.gz
install -Dm644 Gnuplot.txt %{buildroot}%{_docdir}/iozone/Gnuplot.txt

install -Dm644 $RPM_BUILD_DIR/iozone%{version}/docs/iozone.1 %{buildroot}%{_mandir}/man1/iozone.1

%files
%{_bindir}/iozone
%{_bindir}/fileop
%{_bindir}/pit_server
%{_bindir}/Generate_Graphs
%{_bindir}/gengnuplot.sh
%{_bindir}/gnu3d.dem
%{_mandir}/man1/*
%{_docdir}/iozone/

%changelog
%autochangelog
