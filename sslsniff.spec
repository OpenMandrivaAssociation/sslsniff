Summary:	SSL/TLS man-in-the-middle attack tool
Name:		sslsniff
Version:	0.7
Release:	%mkrel 1
License:	GPLv3+
Group:		System/Servers
URL:		http://www.thoughtcrime.org/software/sslsniff/
Source0:	http://www.thoughtcrime.org/software/sslsniff/%{name}-%{version}.tar.gz
Requires:	openssl
BuildRequires:	openssl-devel
BuildRequires:	boost-devel
BuildRequires:	log4cpp-devel >= 1.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
sslsniff is designed to create man-in-the-middle (MITM) attacks for SSL/TLS
connections, and dynamically generates certs for the domains that are being
accessed on the fly. The new certificates are constructed in a certificate
chain that is signed by any certificate that is provided. sslsniff also
supports other attacks like null-prefix or OCSP attacks to achieve silent
interceptions of connections when possible.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README
%attr(0755,root,root) %{_bindir}/sslsniff

