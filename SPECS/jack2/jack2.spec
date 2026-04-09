# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jack2
Version:        1.9.22
Release:        %autorelease
Summary:        The Jack Audio Connection Kit
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/jackaudio/jack2
#!RemoteAsset:  sha256:1e42b9fc4ad7db7befd414d45ab2f8a159c0b30fcd6eee452be662298766a849
Source0:        https://github.com/jackaudio/jack2/archive/refs/tags/v%{version}.tar.gz

# remove the dep of imp.
Patch0:         0001-remove-imp.patch

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(opus)
BuildRequires:  doxygen
BuildRequires:  systemd-rpm-macros

%description
JACK is a low-latency audio server, written primarily for the Linux operating
system. It can connect a number of different applications to an audio device, as
well as allowing them to share audio between themselves. Its clients can run in
their own processes (i.e. as a normal application), or can they can run within a
JACK server (i.e. a "plugin").

%package        devel
Summary:        Header files for Jack
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files for the Jack Audio Connection Kit.

%prep
%autosetup -p1 -n %{name}-%{version}

%conf
export PREFIX=%{_prefix}
python3 ./waf configure \
   --mandir=%{_mandir}/man1 \
   --libdir=%{_libdir} \
   --doxygen \
   --dbus \
   --classic \
   --alsa \
   --clients 256 \
   --ports-per-application=2048

%build
%set_build_flags
python3 ./waf build %{?_smp_mflags} -v

%install
python3 ./waf --destdir=%{buildroot} install
mv %{buildroot}%{_datadir}/jack-audio-connection-kit %{buildroot}%{_docdir}

%files
%doc ChangeLog.rst README.rst README_NETJACK2
%license COPYING
%{_bindir}/jackd
%{_libdir}/jack/
%{_libdir}/libjack.so.*
%{_libdir}/libjackserver.so.*
%{_mandir}/man1/jackd*.1*
%{_bindir}/jackdbus
%{_datadir}/dbus-1/services/org.jackaudio.service
%{_bindir}/jack_control

%files devel
%{_docdir}/reference/html/
%{_includedir}/jack/
%{_libdir}/libjack.so
%{_libdir}/libjackserver.so
%{_libdir}/pkgconfig/jack.pc

%changelog
%autochangelog
