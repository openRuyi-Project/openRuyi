# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# We don't have these yet
# If we have these, change the default to 1
%bcond gnome 0
%bcond gtk2 0
%bcond qt6 0
%bcond kf6 0
# Remember password
%bcond libsecret 0

Name:           pinentry
Version:        1.3.2
Release:        %autorelease
Summary:        Collection of simple PIN or passphrase entry dialogs
License:        GPL-2.0-or-later
URL:            https://gnupg.org/
VCS:            git:https://git.gnupg.org/pinentry.git
#!RemoteAsset
Source0:        %{url}/ftp/gcrypt/%{name}/%{name}-%{version}.tar.bz2
#!RemoteAsset
Source1:        %{url}/ftp/gcrypt/%{name}/%{name}-%{version}.tar.bz2.sig
# We need this wrapper
Source2:        pinentry
BuildSystem:    autotools

BuildOption(conf):  --disable-rpath
BuildOption(conf):  --disable-dependency-tracking
BuildOption(conf):  --enable-pinentry-gnome3
%if %{with gtk2}
BuildOption(conf):  --enable-pinentry-gtk2
%else
BuildOption(conf):  --disable-pinentry-gtk2
%endif
%if %{with qt6}
BuildOption(conf):  --enable-pinentry-qt
%else
BuildOption(conf):  --disable-pinentry-qt
%endif
BuildOption(conf):  --disable-pinentry-qt5
BuildOption(conf):  --enable-pinentry-emacs
BuildOption(conf):  --enable-pinentry-tty
%if %{with libsecret}
BuildOption(conf):  --enable-libsecret
%else
BuildOption(conf):  --disable-libsecret
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  pkgconfig(libassuan)
%if %{with gnome}
BuildRequires:  pkgconfig(gcr-4)
%endif
%if %{with libsecret}
BuildRequires:  pkgconfig(libsecret-1)
%endif
%if %{with gtk2}
BuildRequires:  pkgconfig(gtk+-2.0)
%endif
%if %{with qt6}
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  desktop-file-utils
%endif
%if %{with kf6}
BuildRequires:  pkgconfig(KF6WindowSystem)
BuildRequires:  pkgconfig(KF6GuiAddons)
%endif

Provides:       %{name}-curses = %{version}-%{release}

%description
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the curses (text) based version of the PIN entry dialog.

%if %{with gnome}
%package        gnome3
Summary:        Passphrase/PIN entry dialog for GNOME 3
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-gui = %{version}-%{release}

%description    gnome3
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the GNOME 3 version of the PIN entry dialog.
%endif

%if %{with gtk2}
%package        gtk
Summary:        Passphrase/PIN entry dialog based on GTK+
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-gui = %{version}-%{release}
Provides:       pinentry-gtk2 = %{version}-%{release}

%description    gtk
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the GTK GUI based version of the PIN entry dialog.
%endif

%if %{with qt6}
%package        qt
Summary:        Passphrase/PIN entry dialog based on Qt6
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-gui = %{version}-%{release}
Provides:       pinentry-qt6 = %{version}-%{release}
%if ! %{with gtk2}
# Special case to handle replacement of "default" pinentry implementation
Obsoletes:      %{name}-gtk < %{version}-%{release}
%endif

%description    qt
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the Qt6 GUI based version of the PIN entry dialog.
%endif

%package        emacs
Summary:        Passphrase/PIN entry dialog based on emacs
Requires:       %{name} = %{version}-%{release}

%description    emacs
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the emacs based version of the PIN entry dialog.

%package        tty
Summary:        Passphrase/PIN entry dialog in tty
Requires:       %{name} = %{version}-%{release}

%description    tty
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the tty version of the PIN entry dialog.

%conf -p
export ACLOCAL_PATH=/usr/share/gettext/m4/
autoreconf -fiv

%install -a
# Symlink for Backward compatibility
%if %{with gtk2}
ln -s pinentry-gtk-2 $RPM_BUILD_ROOT%{_bindir}/pinentry-gtk
%endif
%if %{with qt6}
ln -s pinentry-qt $RPM_BUILD_ROOT%{_bindir}/pinentry-qt4
ln -s pinentry-qt $RPM_BUILD_ROOT%{_bindir}/pinentry-qt5
%endif
install -p -m755 -D %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/pinentry
# unpackaged files
rm -fv $RPM_BUILD_ROOT%{_infodir}/dir
%if %{with qt6}
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnupg.pinentry-qt.desktop
%endif
install -d %{buildroot}%{_datadir}/pixmaps

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/pinentry-curses
%{_bindir}/pinentry
%{_infodir}/pinentry.info*

%if %{with gnome}
%files gnome3
%{_bindir}/pinentry-gnome3
%endif

%if %{with gtk2}
%files gtk
%{_bindir}/pinentry-gtk-2
# symlink for backward compatibility
%{_bindir}/pinentry-gtk
%endif

%if %{with qt6}
%files qt
%{_bindir}/pinentry-qt
# symlinks for backward compatibility
%{_bindir}/pinentry-qt4
%{_bindir}/pinentry-qt5
%{_datadir}/applications/org.gnupg.pinentry-qt.desktop
%{_datadir}/pixmaps/pinentry.png
%endif

%files emacs
%{_bindir}/pinentry-emacs

%files tty
%{_bindir}/pinentry-tty

%changelog
%autochangelog
