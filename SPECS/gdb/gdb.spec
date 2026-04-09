# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Disable LTO until upstream fixes GDB's ODR woes.
%define _lto_cflags %{nil}

Name:           gdb
Version:        17.1
Release:        %autorelease
Summary:        A GNU source-level debugger for C, C++, Fortran, Go and other languages
License:        GPL-3.0-only WITH GCC-exception-3.1 AND GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND MIT
URL:            https://www.gnu.org/software/gdb/
VCS:            git:https://sourceware.org/git/binutils-gdb.git
#!RemoteAsset:  sha256:2b93c4c9726a4b8cfe771036e155377405dfa41c483d90945481319c5663c120
Source0:        https://ftpmirror.gnu.org/gnu/gdb/gdb-%{version}.tar.gz
Source2:        gdbinit
BuildSystem:    autotools

BuildOption(conf):  --disable-nls
BuildOption(conf):  --disable-sim
BuildOption(conf):  --with-system-readline
BuildOption(conf):  --with-python=%{__python3}
BuildOption(conf):  --with-gdb-datadir=%{_datadir}/gdb
BuildOption(conf):  --with-system-gdbinit=%{_sysconfdir}/gdbinit
BuildOption(conf):  --enable-source-highlight
BuildOption(conf):  --enable-tui
BuildOption(conf):  --enable-languages=all
BuildOption(conf):  --enable-multilib
BuildOption(conf):  --enable-build-with-cxx

BuildRequires:  texinfo
BuildRequires:  flex
BuildRequires:  python3-devel
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(source-highlight)

%description
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Fortran, Go, and other languages, by executing them in a controlled
fashion and printing their data.

If you want to use GDB for development purposes, you should install
the 'gdb' package which will install 'gdb-headless' and possibly other
useful packages too.

%package        gdbserver
Summary:        A standalone server for GDB (the GNU source-level debugger)

%description    gdbserver
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Fortran, Go, and other languages, by executing them in a controlled
fashion and printing their data.

This package provides a program that allows you to run GDB on a different
machine than the one which is running the program being debugged.

%package        doc
Summary:        Documentation for GDB (the GNU source-level debugger)
License:        GFDL
BuildArch:      noarch
Requires(post): /usr/sbin/install-info
Requires(preun): /usr/sbin/install-info

%description    doc
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Java, and other languages, by executing them in a controlled fashion
and printing their data.

This package provides INFO, HTML and PDF user manual for GDB.

%install -a
# Copy the <sourcetree>/gdb/NEWS file to the directory above it.
cp $RPM_BUILD_DIR/%{name}-%{version}/gdb/NEWS $RPM_BUILD_DIR/%{name}-%{version}/

mkdir -p %{buildroot}%{_prefix}/libexec
mv -f %{buildroot}%{_bindir}/gdb %{buildroot}%{_prefix}/libexec/gdb
ln -s -r %{buildroot}%{_prefix}/libexec/gdb  %{buildroot}%{_bindir}/gdb

mkdir -p %{buildroot}%{_sysconfdir}/gdbinit.d
touch -r %{SOURCE2} %{buildroot}%{_sysconfdir}/gdbinit.d
sed 's#%%{_sysconfdir}#%{_sysconfdir}#g' <%{SOURCE2} >%{buildroot}%{_sysconfdir}/gdbinit
touch -r %{SOURCE2} %{buildroot}%{_sysconfdir}/gdbinit

for i in `find %{buildroot}%{_datadir}/gdb/python/gdb -name "*.py"`
do
  # Files could be also patched getting the current time.
  touch -r $RPM_BUILD_DIR/%{name}-%{version}/gdb/version.in $i
done

%py_byte_compile %{__python3} %{buildroot}%{_datadir}/gdb/python/gdb

# /usr/share/gdb/auto-load/ needs filesystem symlinks
for i in $(echo bin lib $(basename %{_libdir}) sbin|tr ' ' '\n'|sort -u);do
  # mkdir to satisfy dangling symlinks build check.
  mkdir -p %{buildroot}%{_datadir}/gdb/auto-load/%{_root_prefix}/$i
  ln -s $(echo %{_root_prefix}|sed 's#^/*##')/$i \
        %{buildroot}%{_datadir}/gdb/auto-load/$i
done
for i in `find %{buildroot}%{_datadir}/gdb -name "*.py"`; do
  # Files are installed by install(1) not preserving the timestamps.
  touch -r $RPM_BUILD_DIR/%{name}-%{version}/gdb/version.in $i
done

# Create the folder where GDB expects to find custom JIT readers.
mkdir -p %{buildroot}%{_libdir}/gdb

# Remove the files that are part of a gdb build but that are owned and
# provided by other packages.
# These are part of binutils
rm -rf %{buildroot}%{_datadir}/locale/
rm -f %{buildroot}%{_infodir}/bfd*
rm -f %{buildroot}%{_infodir}/standard*
rm -f %{buildroot}%{_infodir}/configure*
rm -f %{buildroot}%{_infodir}/sframe-spec*
# Just exclude the header files in the top directory, and don't exclude
# the gdb/ directory, as it contains jit-reader.h.
rm -rf %{buildroot}%{_includedir}/*.h
rm -rf %{buildroot}/%{_libdir}/lib{bfd*,opcodes*,iberty*,ctf*,sframe*}

# pstack obsoletion
ln -s gstack.1 %{buildroot}%{_mandir}/man1/pstack.1
ln -s gstack %{buildroot}%{_bindir}/pstack

# Packaged GDB is not a cross-target one.
(cd %{buildroot}%{_datadir}/gdb/syscalls
rm -f mips*.xml
rm -f sparc*.xml
rm -f amd64-linux.xml
rm -f i386-linux.xml
rm -f s390*.xml
rm -f ppc*.xml
rm -f aarch64-linux.xml
rm -f arm-linux.xml
rm -f freebsd.xml
rm -f loongarch-linux.xml
rm -f freebsd.xml
)

# Documentation only for development.
rm -f %{buildroot}%{_infodir}/gdbint*
rm -f %{buildroot}%{_infodir}/stabs*
rm -f %{buildroot}%{_infodir}/ctf-spec*

# Delete this too because the dir file will be updated at rpm install time.
# We don't want a gdb specific one overwriting the system wide one.
rm -f %{buildroot}%{_infodir}/dir

# TODO: Fix tests.
%check

%pre
for i in $(echo bin lib $(basename %{_libdir}) sbin|tr ' ' '\n'|sort -u);do
  src="%{_datadir}/gdb/auto-load/$i"
  dst="%{_datadir}/gdb/auto-load/%{_root_prefix}/$i"
  if test -d $src -a ! -L $src;then
    if ! rmdir 2>/dev/null $src;then
      mv -n $src/* $dst/
      rmdir $src
    fi
  fi
done

%post doc
# This step is part of the installation of the RPM. Not to be confused
# with the 'make install ' of the build (rpmbuild) process.

# For --excludedocs:
if [ -e %{_infodir}/gdb.info.gz ]
then
  /usr/sbin/install-info --info-dir=%{_infodir} %{_infodir}/annotate.info.gz || :
  /usr/sbin/install-info --info-dir=%{_infodir} %{_infodir}/gdb.info.gz || :
fi

%preun doc
if [ $1 = 0 ]
then
  # For --excludedocs:
  if [ -e %{_infodir}/gdb.info.gz ]
  then
    /usr/sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/annotate.info.gz || :
    /usr/sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/gdb.info.gz || :
  fi
fi

%files
%license COPYING3 COPYING COPYING.LIB COPYING3.LIB
%doc README NEWS
%{_bindir}/gdb
%{_bindir}/gcore
%{_mandir}/*/gcore.1*
%{_bindir}/gstack
%{_mandir}/*/gstack.1*
%{_bindir}/pstack
%{_mandir}/*/pstack.1*
# Provide gdb/jit-reader.h so that users are able to write their own GDB JIT
# plugins.
%{_includedir}/gdb
# Export the folder where JIT readers should be placed.
%dir %{_libdir}/gdb
%{_prefix}/libexec/gdb
%config(noreplace) %{_sysconfdir}/gdbinit
%{_mandir}/*/gdb.1*
%{_sysconfdir}/gdbinit.d
%{_mandir}/*/gdbinit.5*
%{_bindir}/gdb-add-index
%{_mandir}/*/gdb-add-index.1*
%{_datadir}/gdb

%files gdbserver
%{_bindir}/gdbserver
%{_mandir}/*/gdbserver.1*
%ifarch x86_64
%{_libdir}/libinproctrace.so
%endif

%files doc
%{_infodir}/annotate.info*
%{_infodir}/gdb.info*

%changelog
%autochangelog
